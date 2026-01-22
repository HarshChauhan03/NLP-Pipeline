text = "This is a simple example to understand stopwords in NLP"

stopwords = {"is", "a", "to", "in", "this"}

words = text.lower().split()
filtered_words = [w for w in words if w not in stopwords]

print("Original Words:", words)
print("After Stopwords Removal:", filtered_words)
print("Final Text:", " ".join(filtered_words))
