import re

text = "NLP is amazing. It helps computers understand human language!"

# Sentence Tokenization
sentences = re.split(r'[.!?]+', text)
sentences = [s.strip() for s in sentences if s.strip()]

# Word Tokenization
words = re.findall(r'\b\w+\b', text.lower())

print("Sentences:")
for s in sentences:
    print("-", s)

print("\nWords:")
print(words)
print("\nTotal words:", len(words))
