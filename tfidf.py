import math
import string
from textblob import TextBlob as tb

with open('vegetarianenglishtrimmed.txt', 'r') as myfile:
    veg=myfile.read().replace('\n', '')

with open('11-0.txt', 'r') as myfile:
    x=myfile.read().replace('\n', '')

with open('1342-0.txt', 'r') as myfile:
    y=myfile.read().replace('\n', '')

with open('76-0.txt', 'r') as myfile:
    z=myfile.read().replace('\n', '')

veg = veg.replace("'s", "")
x = x.replace("'s", "")
y = y.replace("'s", "")
z = z.replace("'s", "")

veg=veg.lower()
x=x.lower()
y=y.lower()
z=z.lower()

document1 = tb(veg)
document2 = tb(x)
document3 = tb(y)
document4 = tb(z)

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)


def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)


def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))


def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


bloblist = [document1, document2, document3, document4]
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:110]:
        print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))