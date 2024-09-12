import pandas as pd
import numpy as np
import collections
import re
from sklearn.feature_extraction.text import CountVectorizer

# Implement by hands

# doc1 = "Harry Potter is an amazing movie!!"
# doc2 = "Harry Potter is the best movie!"
# doc3 = "Harry Potter is so great"

# doc1 = re.sub(r"[^a-zA-Z0-9]", " ", doc1.lower()).split()
# doc2 = re.sub(r"[^a-zA-Z0-9]", " ", doc2.lower()).split()
# doc3 = re.sub(r"[^a-zA-Z0-9]", " ", doc3.lower()).split()

# Perform bag of words

# all_words = set(doc1 + doc2 + doc3)

# def BOWrepresentation(all_words, doc):
#   bow = dict.fromkeys(all_words, 0)
#   for word in doc:
#     bow[word] = doc.count(word)
#   return bow
#
# bow1 = BOWrepresentation(all_words, doc1)
# bow2 = BOWrepresentation(all_words, doc2)
# bow3 = BOWrepresentation(all_words, doc3)

# tạo DataFrame
# df_bow = pd.DataFrame([bow1, bow2, bow3])
# print(df_bow)

# Using scikit learn to using bag of words
cv = CountVectorizer(binary=True) # counting of how many times a word is being used
doc1 = "Harry Potter is an amazing movie!!"
doc2 = "Harry Potter is the best movie!"
doc3 = "Harry Potter is so great"
cv_out = cv.fit_transform([doc1, doc2, doc3])


print(pd.DataFrame(cv_out.toarray(), columns= cv.get_feature_names_out()))