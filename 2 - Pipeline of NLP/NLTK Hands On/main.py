import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download("averaged_perceptron_tagger")
nltk.download('stopwords')
stopwords = stopwords.words('english')


text = "My Youth Romantic Comedy Is Wrong, as I Expected , Hepburn: Yahari Ore no Seishun Rabukome wa Machigatteiru, abbreviated as Oregairu, and also known as My Teen Romantic Comedy SNAFU, is a Japanese light novel series written by Wataru Watari and illustrated by Ponkan. The series follows Hachiman Hikigaya, a pessimistic, closeminded, and realistic teen, who is forced by his teacher to join the school's service club and work with two girls with issues of their own. They offer help and advice to others while dealing with their inner conflicts."

ml_token = nltk.word_tokenize(text)

# Gắn tag cho các token
# for token in ml_token:
#   print(nltk.pos_tag([token]))

filter_data = [w for w in ml_token if not w in stopwords]
print(filter_data)