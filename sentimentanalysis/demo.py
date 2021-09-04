from __future__ import print_function
from process_data import process_data
from sklearn.naive_bayes import MultinomialNB
import numpy as np
from vob import pos_vob , neg_vob 
from pyvi import ViTokenizer

sum_data = pos_vob + neg_vob
pos_len = len(pos_vob)
neg_len = len(neg_vob)
pos_prob = pos_len/(pos_len+neg_len)
neg_prob = neg_len/(pos_len+neg_len)



def calc(word,category):
	if word in pos_vob:
		return 1
	else:
		return 0

def weighted_prob(word,category):
	basic = calc(word)
	if word in feature_set:
		tot=sum(feature_set[word].values())
	else:
		tot=0
	weight_prob=((1.0*0.5)+(tot*basic_prob))/(1.0+tot)
	return weight_prob
def test_prob(test,category):
	text = ViTokenizer.tokenize(test)
	data=[]
	for i in text:
		if ' ' in i:
			i=i.split(' ')
			for j in i:
				if j not in data:
					data.append(j.lower())
		elif len(i) > 2 and i not in data:
			data.append(i.lower())

	p=1
	for i in data:
		p*=weighted_prob(i,category)
	return p
def naive_bayes(test):
	results={}
	for i in range(0,2):
	text = ViTokenizer.tokenize(test)
	for i in text:

# label = []
# for i in pos_vob:
# 	label.append('1')
# for i in neg_vob:
# 	label.append('0')	
# label = np.array(label)
# clf = MultinomialNB()
# # training 
# clf.fit(data, label)

# test = "tôi nghĩ nó  tốt nhưng nó vẫn xấu"
# text = process_data(test)
# text = ViTokenizer.tokenize(test)
# bag = np.zeros(len_sum, dtype=np.float32)
# for idx, w in enumerate(sum_data):
#         if w in text: 
#             bag[idx] = 1
# bag = np.array([bag])
# print('Predicting class of d5:', clf.predict_proba(bag))
# print(len_sum)
# print(pos_len)
# print(neg_len)

# pos_prob = pos_len/(pos_len+neg_len)
# neg_prob = neg_len/(pos_len+neg_len)