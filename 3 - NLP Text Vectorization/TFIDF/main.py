# Stopwords - score will be less
# unique words repeated in sentence - score will be high

import pandas as pd
import math
import sklearn
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
stopwords.words('english')

first_sent = "Data science is an Amazing career in the current world"
second_sent = "Deep learning is subset of machine learning"

# first_sent = first_sent.split(" ")
# second_sent = second_sent.split(" ")
#
# vocab = set(first_sent).union(set(second_sent))
#
# wordDict1 = dict.fromkeys(vocab, 0)
# wordDict2 = dict.fromkeys(vocab, 0)
#
# for word in first_sent:
#   wordDict1[word] += 1
#
# for word in second_sent:
#   wordDict2[word] += 1
#
# df = pd.DataFrame([wordDict1, wordDict2])
# print(df)

#tf = freq of a word in a document/total number of words in a document

# def calculateTF(wordDict,doc) :
#   tfDict = {}
#   len_corpus = len(doc)
#
#   for word, count in wordDict.items():
#     tfDict[word] = count / len_corpus
#
#   return tfDict
#
# tf1 = calculateTF(wordDict1,first_sent)
# tf2 = calculateTF(wordDict2,second_sent)
#
# tf = pd.DataFrame([tf1, tf2])
#
# f1 = [word for word in wordDict1 if word not in stopwords.words('english')]
# f2 = [word for word in wordDict2 if word not in stopwords.words('english')]

# def caculateIDF(doc) :
#   idfDict = {}
#   len_corpus = len(doc)
#
#   idfDict = dict.fromkey(doc[0].keys(), 0)
#   for word, val in idfDict.items() :
#     idfDict[word] = math.log(len_corpus / float(val) + 1)
#   return idfDict

vec = TfidfVectorizer()
result = vec.fit_transform([first_sent,second_sent])
print(pd.DataFrame(result.toarray(), columns=vec.get_feature_names_out()))