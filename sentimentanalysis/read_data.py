import re
import numpy as np
import json

with open('data/contractions.json', 'r',encoding = "utf8") as f:
    contractions_dict = json.load(f)
contractions = contractions_dict['contractions']
def emoji(review):
    # Smile -- :), : ), :-), (:, ( :, (-:, :') , :O
    review = re.sub(r'(:\s?\)|:-\)|\(\s?:|\(-:|:\'\)|:O)', ' positiveemoji ', review)
    # Laugh -- :D, : D, :-D, xD, x-D, XD, X-D
    review = re.sub(r'(:\s?D|:-D|x-?D|X-?D)', ' positiveemoji ', review)
    # Love -- <3, :*
    review = re.sub(r'(<3|:\*)', ' positiveemoji ', review)
    # Wink -- ;-), ;), ;-D, ;D, (;,  (-; , @-)
    review = re.sub(r'(;-?\)|;-?D|\(-?;|@-\))', ' positiveemoji ', review)
    # Sad -- :-(, : (, :(, ):, )-:, :-/ , :-|
    review = re.sub(r'(:\s?\(|:-\(|\)\s?:|\)-:|:-/|:-\|)', ' negetiveemoji ', review)
    # Cry -- :,(, :'(, :"(
    review = re.sub(r'(:,\(|:\'\(|:"\()', ' negetiveemoji ', review)
    return review

def process_review(review):
    review = review.lower()
    #review = re.sub(r"\d+", " ", str(review)) # Xóa tất cả các số
    review = emoji(review)
    review = re.sub(r"\b[a-zA-Z]\b", "", str(review))
    for word in review.split():
        if word.lower() in contractions:
            review = review.replace(word, contractions[word.lower()])
    review = re.sub(r"[^\w\s]", " ", str(review)) 
    review = re.sub(r'(.)\1+', r'\1', review) #Chuyển nhiều hơn 1 chữu về 1 chữ
    review = re.sub(r"\s+", " ", str(review)) #Chuyển nhiều khoảng trắng về 1 khoảng trắng
    return review
def read_data(path_data):
	pos=open(path_data+"positive.txt","r",encoding = "utf8")
	p = []
	for x in pos:
		x = re.sub("\n|\r", "", x)
		p.append(x)
	positive = np.vectorize(process_review)(p)
	neg=open(path_data+"negative.txt","r",encoding = "utf-8")
	n = []
	for x in neg:
		x = re.sub("\n|\r", "", x)
		n.append(x)
	negative = np.vectorize(process_review)(n)
	neu=open(path_data+"neutral.txt","r",encoding = "utf8")
	ne = []
	for x in neu:
		x = re.sub("\n|\r", "", x)
		ne.append(x)
	neutral = np.vectorize(process_review)(ne)
	return positive, negative , neutral
