import gensim
from textdistance import Levenshtein
import pandas as pd
from xarray.util.generate_aggregations import min_count

df = pd.read_csv("./20191226-reviews.csv")

# Preprocessing & Tokenization
# Kiểm tra và chỉ áp dụng hàm simple_preprocess cho những giá trị không phải NaN hoặc kiểu float
review_text = df['body'].apply(lambda x: gensim.utils.simple_preprocess(str(x)) if isinstance(x, str) else [])
# print(review_text.head())

# Train the Word2Vec Model
model = gensim.models.Word2Vec(window=10, vector_size=100, min_count=2, sg=1)


# Build the Vocabulary
model.build_vocab(review_text)

# Số lần train
print(model.epochs)

# Train Word2Vec Model
model.train(review_text, total_examples=model.corpus_count, epochs=model.epochs)

# Save model
model.save('C:\\Users\\PC\\Desktop\\Models\\skip_gram_model.bin')

