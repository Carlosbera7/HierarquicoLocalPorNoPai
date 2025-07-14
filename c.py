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
            'Sexism': ['Women', 'Men', 'Trans.women', 'Feminists', 'Fat.women', 'Transexuals', 'Ugly.women'],
            'Body': ['Fat.people', 'Fat.women', 'Ugly.people', 'Ugly.women'],
            'Racism': ['Black.people'],
            'Ideology': ['Left.wing.ideology', 'Feminists'],
            'Homophobia': ['Gays', 'Homossexuals', 'Lesbians'],
            'Origin': [],
            'Religion': ['Islamists', 'Muslims'],
            'Migrants': ['Immigrants', 'Refugees'],
            'OtherLifestyle': []
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
            logging.info(f"📊 Relatório para '{child}':\n{classification_report(y_test_filtered, y_pred_child)}")

def gerar():
    X, y = load_and_prepare_data('2019-05-28_portuguese_hate_speech_hierarchical_classification.csv')
    if X is None or y is None:
        return

    y = filter_labels(y)
    label_columns = y.columns.tolist()
    logging.info(f"✅ Rótulos mantidos após filtragem: {label_columns}")

    vectorizer = TfidfVectorizer(max_features=5000)
    X_tfidf = vectorizer.fit_transform(X)

    X_train, y_train, X_test, y_test = iterative_train_test_split(X_tfidf, y.values, test_size=0.3)
    logging.info(f"📐 Partições: X_train: {X_train.shape}, y_train: {y_train.shape}, X_test: {X_test.shape}, y_test: {y_test.shape}")

    train_and_predict_topdown(X_train, y_train, X_test, y_test, label_columns)

if __name__ == "__main__":
    gerar()
