import re
from pyvi import ViTokenizer

def read_data(path_data_1,path_data_2,path_data_3):
	read_1 = open(path_data_1,'r',encoding = 'utf-8')
	read_1 = read_1.readlines()
	data_1 = [i.replace("\n","") for i in read_1]
	data_1 = [re.sub(r"\s+", " ", str(i)) for i in data_1]
	read_2 = open(path_data_2,'r',encoding = 'utf-8')
	read_2 = read_2.readlines()
	data_2 = [i.replace("\n","") for i in read_2]
	data_2 = [re.sub(r"\s+", " ", str(i)) for i in data_2]
	read_3 = open(path_data_3,'r',encoding = 'utf-8')
	read_3 = read_3.readlines()
	data_3 = [i.replace("\n","") for i in read_3]
	data_3 = [re.sub(r"\s+", " ", str(i)) for i in data_3]
	return data_1, data_2, data_3
path_data_1 = 'sentimentanalysis/positive.txt'
path_data_2 = 'sentimentanalysis/negative.txt'
path_data_3 = 'sentimentanalysis/not.txt'
a , b , c = read_data(path_data_1,path_data_2,path_data_3)

pos_vob = [ViTokenizer.tokenize(text) for text in a]
neg_vob = [ViTokenizer.tokenize(text) for text in b]
not_vob = [ViTokenizer.tokenize(text) for text in c]