from hiclass import LocalClassifierPerParentNode
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd

hierarchy = {
    "Hate speech": [],
    "Ageing": ["Hate speech"],
    "Sexism": ["Hate speech"],
    "Women": ["Sexism"],
    "Men": ["Sexism"],
    "Transexuals": ["Sexism"],
    "Homophobia": ["Hate speech"],
    "Homossexuals": ["Homophobia"],
    "Lesbians": ["Homossexuals", "Women"],
    "Gays": ["Homossexuals"],
    "Bissexuals": ["Homophobia"],
    "Body": ["Hate speech"],
    "Fat people": ["Body"],
    "Fat women": ["Women", "Fat people"],
    "Ugly people": ["Body"],
    "Ugly women": ["Women", "Ugly people"],
    "Thin people": ["Body"],
    "Thin women": ["Women", "Thin people"],
    "Old people": ["Ageing"],
    "Old women": ["Women", "Old people"],
    "Young people": ["Ageing"],
    "Racism": ["Hate speech"],
    "Black people": ["Racism"],
    "Black Women": ["Women", "Black people"],
    "White people": ["Racism"],
    "Latins": ["Racism", "Origin"],
    "Asians": ["Racism", "Origin"],
    "Indigenous": ["Racism"],
    "Africans": ["Origin"],
    "South Americans": ["Origin"],
    "Brazilians": ["South Americans"],
    "Brazilians women": ["Women", "South Americans"],
    "Migrants": ["Hate speech"],
    "Refugees": ["Migrants"],
    "Immigrants": ["Migrants"],
    "Origin": ["Hate speech"],
    "Arabic": ["Origin"],
    "Iranians": ["Arabic"],
    "Egyptians": ["Arabic"],
    "Chinese": ["Asians"],
    "Japaneses": ["Asians"],
    "Ucranians": ["East europeans"],
    "Russians": ["East europeans"],
    "Religion": ["Hate speech"],
    "Muslims": ["Religion"],
    "Islamists": ["Religion"],
    "Muslim women": ["Muslims", "Women"],
    "Jews": ["Religion"],
    "Ideology": ["Hate speech"],
    "Left wing ideology": ["Ideology"],
    "Feminists": ["Ideology", "Sexism"],
    "Men Feminists": ["Feminists", "Men"],
    "OtherLifestyle": ["Hate speech"],
    "Football players women": ["Women", "OtherLifestyle"],
    "Gamers": ["OtherLifestyle"],
    "Vegetarians": ["OtherLifestyle"],
    "Street artists": ["OtherLifestyle"],
    "Polyamorous": ["OtherLifestyle"],
    "Criminals": ["OtherLifestyle"],
    "Poor people": ["OtherLifestyle"],
    "Homeless": ["OtherLifestyle"],
    "Homeless women": ["Women", "Homeless"],
    "Health": ["Hate speech"],
    "Disabled people": ["Health"],
    "Autists": ["Health"],
    "Aborting women": ["Women"],
    "Trans women": ["Women", "Transexuals"],
    "Travestis": ["Women"],
    "Sertanejos": ["Rural people", "Brazilians"],
    "Nordestines": ["Rural people", "Brazilians"],
    "Venezuelans": ["Latins"],
    "Argentines": ["Latins"],
    "Mexicans": ["Latins"],
    "Angolans": ["Africans"],
    "Fat women": ["Women", "Fat people"],
    "Ugly women": ["Women", "Ugly people"],
    "Thin women": ["Women", "Thin people"],
    "OtherLifestyle": ["Hate speech"],
    "Ageing": ["Hate speech"],
    "Africans": ["Origin"],
}

data = pd.read_csv("2019-05-28_portuguese_hate_speech_hierarchical_classification.csv")  # Substitua pelo caminho do arquivo

def build_hierarchy(row):
    levels = []
    for col, value in row.items():
        if col in hierarchy and value == 1:
            levels.append(col)
    if not levels:
        levels.append("No.hate.speech")
    return levels

data["hierarchy"] = data.apply(build_hierarchy, axis=1)

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

