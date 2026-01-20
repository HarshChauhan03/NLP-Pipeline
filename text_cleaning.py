import re
import string

text = "Hello!!! I'm Harsh 😄. I love NLP & Data Science. Email: harsh@gmail.com #AI"

def clean_text(text):
    text = text.lower()  # lowercase
    text = re.sub(r'\S+@\S+', '', text)  # remove emails
    text = re.sub(r"http\S+|www\S+", "", text)  # remove urls
    text = re.sub(r"\d+", "", text)  # remove numbers
    text = text.translate(str.maketrans("", "", string.punctuation))  # remove punctuation
    text = re.sub(r"\s+", " ", text).strip()  # remove extra spaces
    return text

cleaned = clean_text(text)

print("Original Text:\n", text)
print("\nCleaned Text:\n", cleaned)
