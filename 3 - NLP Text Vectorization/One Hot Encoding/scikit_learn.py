from sklearn.preprocessing import LabelEncoder
doc1 = "dog bites meat"
doc2 = "man eats meat"
doc3 = "dog bites man"

corpus = [doc1.split(), doc2.split(), doc3.split()]
my_overall_data = corpus[0] + corpus[1] + corpus[2]

le = LabelEncoder()
integer_data = le.fit_transform(my_overall_data)
print(f"Integer Values are: {integer_data}")

