# Importar bibliotecas necessárias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from xgboost import XGBClassifier

# Carregar o arquivo CSV
file_path = '2019-05-28_portuguese_hate_speech_hierarchical_classification.csv'  # Atualizar o caminho conforme necessário
data = pd.read_csv(file_path)

# Mapear a hierarquia
root_categories = ["Hate.speech"]
sub_categories = [col for col in data.columns if col not in ["text"] + root_categories]

hierarchy = {root: [] for root in root_categories}
for col in sub_categories:
    if col in ["Sexism", "Racism", "Ideology", "Homophobia", "Origin", "Religion", "Health"]:
        hierarchy["Hate.speech"].append(col)

# Função para dividir dados por nó pai
def split_data_for_node(data, parent_node, child_nodes):
    relevant_columns = ["text", parent_node] + child_nodes
    filtered_data = data[relevant_columns]
    X = filtered_data["text"]
    y = filtered_data[parent_node]
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Dividir os dados e treinar um modelo para cada nó
models = {}
vectorizers = {}
for parent_node in hierarchy.keys():
    # Dividir os dados
    child_nodes = hierarchy[parent_node]
    X_train, X_test, y_train, y_test = split_data_for_node(data, parent_node, child_nodes)
    
    # Vetorizar os textos
    vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)
    vectorizers[parent_node] = vectorizer
    
    # Treinar o modelo XGBoost
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42, n_estimators=50, n_jobs=4)
    model.fit(X_train_vectorized, y_train)
    models[parent_node] = model
    
    # Avaliar o modelo
    y_pred = model.predict(X_test_vectorized)
    print(f"Relatório para {parent_node}:")
    print(classification_report(y_test, y_pred))

# Treinar para todos os nós (raiz e filhos)
all_nodes = set(hierarchy.keys())
for children in hierarchy.values():
    all_nodes.update(children)

for node in all_nodes:
    # Se o nó não está nas colunas do DataFrame, pule
    if node not in data.columns:
        continue
    # Dividir os dados
    X = data["text"]
    y = data[node]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Vetorizar os textos
    vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)
    vectorizers[node] = vectorizer
    
    # Treinar o modelo XGBoost
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42, n_estimators=50, n_jobs=4)
    model.fit(X_train_vectorized, y_train)
    models[node] = model
    
    # Avaliar o modelo
    y_pred = model.predict(X_test_vectorized)
    print(f"Relatório para {node}:")
    print(classification_report(y_test, y_pred))

# Função para classificar hierarquicamente
def classify_hierarchically(data, hierarchy, vectorizers, models):
    results = []
    for index, row in data.iterrows():
        text = row['text']
        path = []
        
        current_node = "Hate.speech"
        while current_node:
            # Vetorizar o texto
            vectorized_text = vectorizers[current_node].transform([text])
            
            # Obter predição e probabilidade
            model = models[current_node]
            prediction = model.predict(vectorized_text)[0]
            prob = model.predict_proba(vectorized_text)[0].max()
            
            # Registrar o nó atual
            path.append((current_node, prediction, prob))
            
            # Verificar os próximos filhos
            if prediction == 1 and current_node in hierarchy:
                # Avançar para os filhos se o nó atual foi positivo
                children = hierarchy[current_node]
                current_node = children[0] if children else None
            else:
                # Parar a descida na hierarquia
                current_node = None
        
        # Adicionar resultados
        results.append({
            'Text': text,
            'Path': path
        })
    
    return pd.DataFrame(results)

# Preparar dados para teste
test_data = pd.DataFrame({'text': data['text'].sample(n=100, random_state=42)})  # Amostra de 50 textos para teste

# Classificar hierarquicamente
hierarchical_results = classify_hierarchically(test_data, hierarchy, vectorizers, models)

# Exibir resultados
pd.set_option('display.max_colwidth', None)
print(hierarchical_results.head(10))
