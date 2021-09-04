import _pickle as cPickle
from keras.preprocessing.sequence import pad_sequences
import pandas as pd
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.utils.np_utils import to_categorical
from keras.layers import LSTM, Dense, TimeDistributed, Embedding, Bidirectional
from keras.models import Model, Input, load_model
from keras_contrib.layers import CRF
from keras_contrib import losses, metrics
from keras.callbacks import ModelCheckpoint
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn_crfsuite.metrics import flat_classification_report
from sklearn.metrics import f1_score
from seqeval.metrics import precision_score, recall_score, f1_score, classification_report
from process import tokenizes

batch_size = 64
epochs = 50
max_len = 100
embedding = 40
with open('word2idx.txt', 'rb') as fid:
     word2idx = cPickle.load(fid)

with open('num_tag.txt', 'rb') as fid:
     num_tag =  cPickle.load(fid)
with open('words.txt', 'rb') as fid:
     words =  cPickle.load(fid)
with open('idx2tag.txt', 'rb') as fid:
     idx2tag =  cPickle.load(fid)
# with open('history.pkl', 'rb') as fid:
#      model =  cPickle.load(fid)

def build_model(num_tags, hidden_size = 28):
    # Model architecture
    input = Input(shape=(max_len,))
    model = Embedding(input_dim=len(words) + 2, output_dim=embedding, input_length=max_len, mask_zero=False)(input)
    model = Bidirectional(LSTM(units=hidden_size, return_sequences=True, recurrent_dropout=0.1))(model)
    model = TimeDistributed(Dense(hidden_size, activation="relu"))(model)
    crf = CRF(num_tags + 1)  # CRF layer
    out = crf(model)  # output
    model = Model(input, out)
    model.compile(optimizer="rmsprop", loss=crf.loss_function, metrics=[crf.accuracy])
    model.summary()
    return model
model = build_model(num_tag)
model.load_weights("model.hdf5")
max_len = 100
def check_name(text):
     result = []
     text = tokenizes(text)
     texts = []
     for i in range(0,len(text)):
          texts.append(text[i])
          if text[i] not in words:
               text[i] = "UNK"
     text =[word2idx[w] for w in text]
     text = pad_sequences(maxlen = max_len, sequences = [text] ,padding = "post", value = word2idx["PAD"])
     per = model.predict(text)
     per = np.argmax(per, axis=-1)
     pred = [idx2tag[i] for i in per[0]]
     for i in range(len(pred)):
          if pred[i] == 'B-PER' or pred[i] == 'I-PER':
               result.append(texts[i])
     result = ' '.join(result)
     return result  
     
def check_address(text):
     result = []
     a = []
     text = tokenizes(text)
     texts = []
     for i in range(0,len(text)):
          texts.append(text[i])
          if text[i] not in words:
               text[i] = 'UNK'
     text =[word2idx[w] for w in text]
     text = pad_sequences(maxlen = max_len, sequences = [text] ,padding = "post", value = word2idx["PAD"])
     per = model.predict(text)
     per = np.argmax(per, axis=-1)
     pred = [idx2tag[i] for i in per[0]]
     for i in range(len(pred)):
          if pred[i] == 'B-LOC' or pred[i] == 'I-LOC':
               a.append(texts[i])
          elif a not in result and len(a) > 1:
               a = ' '.join(a)
               result.append(a)
               a = []
     #result = ' '.join(result)
     return result


text = "tôi sống ở số 4, đường Giải Phóng, quận Hai Bà Trưng"
a = check_address(text)
print(a)