def simple_stem(word):
    suffixes = ["ing", "ed", "ly", "s"]
    for suf in suffixes:
        if word.endswith(suf):
            return word[:-len(suf)]
    return word

words = ["playing", "played", "happily", "cats", "runs"]

stemmed = [simple_stem(w) for w in words]

print("Original Words:", words)
print("Stemmed Words:", stemmed)
