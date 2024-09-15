import gensim
import numpy as np
import pandas as pd
import numpy
from numpy.ma.core import indices

# Load models

model = gensim.models.Word2Vec.load('C:\\Users\\PC\\Desktop\\Models\\skip_gram_model.bin')
# Find the similar Words And Similarity between the words
# Word Embeddings
# print(model.wv.most_similar("stupid"))

# count the similarity between two words
# print(model.wv.similarity(w1="cheap", w2="inexpensive"))

# extract the word embedding matrix
matrix = model.wv.vectors

W_out = model.wv.vectors
W_out.shape # Output weight
# print(W_out.shape)

# Get vocab list
vocab_list = list(model.wv.key_to_index.keys())
#print(vocab_list)
vocab_len = len(vocab_list)

vocab = model.wv.key_to_index

# vocab index -> word

vocab_int2word = {index: word for word, index in vocab.items()}

# tạo vector one hot
one_hot = np.zeros(shape=(1, vocab_len))
# Đặt giá trị one-hot cho từ 'good'
word_index = vocab['good']  # Lấy chỉ số của từ 'good'
one_hot[0, word_index] = 1

z_proj =  np.dot(one_hot, matrix)
z_proj.shape
a_proj = z_proj

z_out = np.dot(a_proj, W_out.T)
# print(z_out.shape)

# Softmax
a_out = np.exp(z_out)/np.sum(np.exp(z_out), axis=1, keepdims=True)
# print(a_out.shape)

a_out = a_out.flatten()
indices = np.argsort(a_out)  # sort in ascending order
indices = indices[::-1] # sort in descending order

for i in range(10) :
  word_index = indices[i]
  word = vocab_int2word[word_index]
  a_out_i = a_out[word_index]
  print(f"{word} with score {a_out_i}")