import pandas as pd
import xgboost as xgb
import re
import nltk
import logging
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from skmultilearn.model_selection import iterative_train_test_split
from scipy.sparse import vstack
from nltk.corpus import stopwords
from iterstrat.ml_stratifiers import MultilabelStratifiedKFold
import pickle
import os

nltk.download('stopwords')

# Configurações de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', str(text).lower())
    stop_words = set(stopwords.words('portuguese'))
    words = [word for word in text.split() if word not in stop_words]
    return ' '.join(words)

def load_and_prepare_data(file_path):
    try:
        logging.info("Carregando os dados...")
        data = pd.read_csv(file_path)
        data['text'] = data['text'].apply(clean_text)
        X = data['text']
        y = data.drop(columns=['text'])
        return X, y
    except FileNotFoundError:
        logging.error(f"Arquivo {file_path} não encontrado.")
        return None, None

def filter_labels(y, min_count=10):
    label_counts = y.sum(axis=0)
    valid_labels = label_counts[label_counts >= min_count].index
    return y[valid_labels]

def train_binary_classifier(X_pos, X_neg, y_pos, y_neg):
    X_train = vstack([X_pos, X_neg])
    y_train = y_pos + y_neg
    model = xgb.XGBClassifier(eval_metric='logloss')
    model.fit(X_train, y_train)
    return model

def train_and_predict_topdown(X_train, y_train, X_test, y_test, label_columns):
    hierarchy = {
        'Hate.speech': {
            'R': ['Hate.speech', 'No.hate.speech'],
            'Hate.speech': ['Homophobia', 'Racism', 'Sexism', 'Body', 'Ideology', 'Religion', 'Migrants', 'OtherLifestyle', 'Origin'],
            'Homophobia': ['Homossexuals'],           
            'Homossexuals': ['Gays', 'Lesbians'],
            'Racism': ['Black.people'],
            'Ideology': ['Left.wing.ideology', 'Feminists'],            
            'Sexism': ['Women', 'Men',  'Feminists', 'Transexuals'],
            'Transexuals': ['Trans.women'],
            'Women': ['Trans.women', 'Fat.women', 'Ugly.women', 'Lesbians'],            
            'Body': ['Fat.people', 'Ugly.people'],
            'Ugly.people': ['Ugly.women'],
            'Fat.people': ['Fat.women'],
            'Migrants': ['Immigrants', 'Refugees'],
            'Religion': ['Islamists', 'Muslims']            
        }
    }

    models = {}
    predictions = {}

    for parent, children in hierarchy['Hate.speech'].items():
        if parent not in label_columns:
            continue

        idx = label_columns.index(parent)
        y_train_col = y_train[:, idx]
        y_test_col = y_test[:, idx]

        pos_train = int((y_train_col == 1).sum())
        neg_train = int((y_train_col == 0).sum())
        logging.info(f"\n🔷 [Nó] {parent} - Treinando com {pos_train} positivos, {neg_train} negativos")

        if pos_train == 0 or neg_train == 0:
            logging.warning(f"⚠️ Ignorando '{parent}' (dados insuficientes)")
            continue

        X_pos = X_train[y_train_col == 1]
        X_neg = X_train[y_train_col == 0]
        y_pos = [1] * X_pos.shape[0]
        y_neg = [0] * X_neg.shape[0]

        model = train_binary_classifier(X_pos, X_neg, y_pos, y_neg)
        models[parent] = model

        # Prever no X_test inteiro
        y_pred_parent = model.predict(X_test)
        predictions[parent] = y_pred_parent
        logging.info(f"\n📊 Relatório para '{parent}':\n{classification_report(y_test_col, y_pred_parent)}")

        for child in children:
            if child not in label_columns:
                logging.warning(f"    ⚠️ Subclasse '{child}' não presente nas colunas")
                continue

            idx_child = label_columns.index(child)
            y_train_child = y_train[:, idx_child]
            y_test_child = y_test[:, idx_child]

            # Treina o modelo filho com todos os dados (não condicionado)
            X_pos = X_train[y_train_child == 1]
            X_neg = X_train[y_train_child == 0]
            y_pos = [1] * X_pos.shape[0]
            y_neg = [0] * X_neg.shape[0]

            if len(y_pos) == 0 or len(y_neg) == 0:
                logging.warning(f"    ⚠️ Ignorando '{child}' (dados insuficientes)")
                continue

            model_child = train_binary_classifier(X_pos, X_neg, y_pos, y_neg)
            models[child] = model_child

            # Agora só prever e avaliar onde o pai previu 1
            mask = (y_pred_parent == 1)
            if mask.sum() == 0:
                logging.warning(f"    ⚠️ Nenhum exemplo para avaliar '{child}' (pai previu 0)")
                continue

            y_pred_child = model_child.predict(X_test[mask])
            y_test_filtered = y_test[mask][:, idx_child]

            logging.info(f"  🔹 [Subnó] {child} - Avaliando {mask.sum()} exemplos condicionados")
            logging.info(f"📊 Relatório para '{child}':\n{classification_report(y_test_filtered, y_pred_child, zero_division=0)}")
            
def gerar_particoes_multilabel(X_tfidf, y, n_splits=10, caminho = 'particoes.pkl'):
    """
    Gera partições estratificadas multilabel com IterativeStratification.
    """
    logging.info(f"📁 Gerando {n_splits} partições multilabel para validação cruzada...")

    mskf = MultilabelStratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    folds = []

    for train_idx, test_idx in mskf.split(X_tfidf, y):
        folds.append((train_idx, test_idx))

    with open(caminho, 'wb') as f:
        pickle.dump(folds, f)

    logging.info(f"✅ Partições salvas em {caminho}")         
    
def executar_cross_validation(X_tfidf, y, label_columns, caminho='particoes.pkl'):
    with open(caminho, 'rb') as f:
        folds = pickle.load(f)

    for i, (train_idx, test_idx) in enumerate(folds):
        logging.info(f"\n========================= 📚 Fold {i+1}/10 =========================")
        X_train, y_train = X_tfidf[train_idx], y[train_idx]
        X_test, y_test = X_tfidf[test_idx], y[test_idx]
        train_and_predict_topdown(X_train, y_train, X_test, y_test, label_columns)       

def gerar():
    X, y = load_and_prepare_data('2019-05-28_portuguese_hate_speech_hierarchical_classification.csv')
    if X is None or y is None:
        return

    y = filter_labels(y)
    label_columns = y.columns.tolist()
    logging.info(f"✅ Rótulos mantidos após filtragem: {label_columns}")

    vectorizer = TfidfVectorizer(max_features=5000)
    X_tfidf = vectorizer.fit_transform(X)

    y = y.values
    if not os.path.exists('particoes.pkl'):
        gerar_particoes_multilabel(X_tfidf, y, n_splits=10)
    
    executar_cross_validation(X_tfidf, y, label_columns)

if __name__ == "__main__":
    gerar()
