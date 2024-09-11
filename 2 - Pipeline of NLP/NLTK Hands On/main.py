import nltk

nltk.download('punkt')

text = "DKM tai sao t phai hoc machine learning?"

ml_token = nltk.word_tokenize(text)

print(list(nltk.bigrams(ml_token)))

print(list(nltk.trigrams(ml_token)))