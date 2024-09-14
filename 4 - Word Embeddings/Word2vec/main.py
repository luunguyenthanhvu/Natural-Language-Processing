import gensim
from random import choice
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

model_path = "C:\\Users\\PC\\Downloads\\archive_text\\GoogleNews-vectors-negative300.bin"

model = gensim.models.keyedvectors.load_word2vec_format(model_path, binary=True)

vocab = list(model.index_to_key)

vector = model.word_vec("Narendra_Modi")

word1 = "Harry"
word2 = "Potter"

score = model.similarity(word1, word2)
print(f"cosine similarity between {word1} and {word2}: {score}")