import pandas as pd
from hiclass import LocalClassifierPerParentNode
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Carregar a base de dados
data = pd.read_csv("2019-05-28_portuguese_hate_speech_hierarchical_classification.csv")  # Substitua pelo caminho do arquivo

# Criar hierarquia das classes
def build_hierarchy(row):
    hierarchy = []
    if row["Hate.speech"] == 1:
        hierarchy.append("Hate.speech")
        for col in ["Sexism", "Racism", "Body", "Ideology", "Homophobia", "Origin", "Religion", "Health", "OtherLifestyle"]:
            if row[col] == 1:
                hierarchy.append(col)
                break  # Considera apenas a primeira categoria (ajuste conforme necessário)
    else:
        hierarchy.append("No.hate.speech")
    return hierarchy

data["hierarchy"] = data.apply(build_hierarchy, axis=1)

# Vetorização do texto
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(data["text"])
y = data["hierarchy"]

# Divisão em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinamento do classificador
classifier = LocalClassifierPerParentNode()
classifier.fit(X_train, y_train)

# Previsão
predictions = classifier.predict(X_test)

# Resultados
for i in range(5):
    print(f"Texto: {data['text'].iloc[i]}")
    print(f"Previsão: {predictions[i]}")
