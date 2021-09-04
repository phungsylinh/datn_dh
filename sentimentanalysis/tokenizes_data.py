import numpy as np
import nltk
import re
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
from  tokenization import dict_models
from read_data import read_data

path_data = 'data/sentiment/'
pos , neg , neu = read_data(path_data)
def tokenize(sentence):
    lm_tokenizer = dict_models.LongMatchingTokenizer()
    tokens = lm_tokenizer.tokenize(sentence)
    return tokens
    
positive = []
negative = []
neutral = []

def tokenize_data(pos,neg,neu):
    for i in range(0,len(pos)):
        a = tokenize(pos[i])
        positive.append(a)
    for i in range(0,len(neg)):
        a = tokenize(neg[i])
        negative.append(a)
    for i in range(0,len(neu)):
        a = tokenize(neu[i])
        neutral.append(a)
    return positive , negative , neutral

def stop_words(lists):
    file = open('data/stop_words.txt', "r",encoding="utf8")
    stop_words = file.read()

    for i in range(len(lists)):
        for j in range(0,len(lists[i])):
            if lists[i][j] in stop_words:
                lists[i][j]=""
        lists[i] = ' '.join(lists[i])
        lists[i] = re.sub(r"\s+", " ", str(lists[i]))
    return lists

def get_data():
    a , b , c = tokenize_data(pos,neg,neu)
    pos_token = stop_words(a)
    neg_token = stop_words(b)
    return pos_token , neg_token

pos_token , neg_token = get_data()
# fh  = open("negative.txt",'w',encoding = "utf8")
# for i in neg_token:
#     fh.write(i + "\n")
# fh.close()
#  