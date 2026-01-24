from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "I love NLP",
    "NLP is a part of AI",
    "I love AI"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

print("Vocabulary:", vectorizer.get_feature_names_out())
print("\nBag of Words Matrix:\n", X.toarray())
