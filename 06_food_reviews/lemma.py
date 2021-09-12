from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import pos_tag

lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words('english')

print(stop_words)

# print(lemmatizer.lemmatize('computer'))
# print(lemmatizer.lemmatize('mice'))

print(pos_tag(['big']))
print(pos_tag(['book']))
print(pos_tag(['large']))