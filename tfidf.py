from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "I love NLP",
    "NLP is a part of AI",
    "I love AI"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

print("Vocabulary:", vectorizer.get_feature_names_out())
print("\nTF-IDF Matrix:\n", X.toarray())
