from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import RegexpStemmer
from nltk.stem import WordNetLemmatizer

import nltk
nltk.download('wordnet')

# porter = PorterStemmer()
#
# words =  ["generous", "generic", "genorously", "generation"]
# for word in words:
#   print(f"{word} --> {porter.stem(word)}")

# snowball = SnowballStemmer(language='english')
#
# words =  ["generous", "generic", "genorously", "generation"]
# for word in words:
#   print(f"{word} --> {snowball.stem(word)}")



# lan = LancasterStemmer()
#
# words =  ["generous", "generic", "genorously", "generation"]
# for word in words:
#   print(f"{word} --> {lan.stem(word)}")

# reg = RegexpStemmer('ing|s$|ables$', min=4)
#
# words =  ["generous", "generic", "genorously", "generation"]
# for word in words:
#   print(f"{word} --> {reg.stem(word)}")


# Khởi tạo WordNetLemmatizer
lema = WordNetLemmatizer()

# Danh sách các từ để lemmatize
words = ["generous", "running", "generic", "generously", "generation"]

# Lematize từng từ và in kết quả
for word in words:
    print(f"{word} --> {lema.lemmatize(word, pos='v')}")