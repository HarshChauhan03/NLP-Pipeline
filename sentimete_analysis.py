from textblob import TextBlob

texts = [
    "I love this product, it is amazing!",
    "This is the worst experience ever.",
    "The movie was okay, not bad."
]

for t in texts:
    blob = TextBlob(t)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😀"
    elif polarity < 0:
        sentiment = "Negative 😡"
    else:
        sentiment = "Neutral 😐"

    print("Text:", t)
    print("Polarity:", polarity)
    print("Sentiment:", sentiment)
    print("-" * 40)
