from sentimentanalysis.process_data import process_data
from sklearn.feature_extraction.text import TfidfVectorizer 
import _pickle as cPickle
from pyvi import ViTokenizer
import re
with open('sentimentanalysis/my_dumped_classifier.pkl', 'rb') as fid:
    gnb_loaded = cPickle.load(fid)

with open('sentimentanalysis/tf.pkl', 'rb') as fid:
    tf = cPickle.load(fid)

with open('sentimentanalysis/stop_words.txt', 'rb') as fid:
    stop_words = cPickle.load(fid)
#tf = TfidfVectorizer(use_idf=True,ngram_range=(1,3))
def process_test(text):
    text = process_data(text)
    return text
def stop_data(text):
    results = []
    for i in range(len(text)):
        text[i] = process_test(text[i])
        text[i] = ViTokenizer.tokenize(text[i]).split()
        for j in range(0,len(text[i])):
            if text[i][j] in stop_words :
                text[i][j]=""
        text[i] = ' '.join(text[i])
        text[i] = re.sub(r"\s+", " ", str(text[i]))
        results.append([text[i]])
    return results
def give_review(text):
    text = stop_data(text)
    for i in text:
        test = tf.transform(i)
        result = gnb_loaded.predict(test)
        if result[0]==0:
            return 'negative'
        else:
            return 'positive'
# text = ["tôi cho là sản phẩm này tệ","xin chào"]
# text = stop_data(text)
# print(text)
# for i in text:
#     test = tf.transform(i)
#     result = gnb_loaded.predict(test)
#     if result[0]==0:
#         print('negative')
#     else:
#         print('positive')
