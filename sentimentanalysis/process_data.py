import re
from sentimentanalysis.replace_file import replaces
from pyvi import ViTokenizer
from sentimentanalysis.vob import pos_vob , neg_vob , not_vob

def process_data(text):
	text = text.lower()
	text = re.sub(r"\b[a-zA-Z]\b", "", str(text))
	for i, j in replaces.items():
		text = text.replace(i,j)
	text = re.sub(r'(.)\1+', r'\1', text) #Chuyển nhiều hơn 1 chữu về 1 chữ
	text = re.sub(r"\s+", " ", str(text)) #Chuyển nhiều khoảng trắng về 1 khoảng trắng
	text = ViTokenizer.tokenize(text)
	texts = text.split()
	texts = [t.replace('_', ' ') for t in texts]
	len_text = len(texts)
	for i in range(len_text):
		cp_text = texts[i]
		if cp_text in not_vob: # Xử lý vấn đề phủ định (VD: không xấu--> notnag)
			numb_word = 2 if len_text - i - 1 >= 4 else len_text - i - 1            
			for j in range(numb_word):
				if texts[i + j + 1] in pos_vob:
					texts[i] = 'notpos'
					texts[i + j + 1] = ''

				if texts[i + j + 1] in neg_vob:
					texts[i] = 'notneg'
					texts[i + j + 1] = ''
	text = u' '.join(texts)
	# xóa ký tự thừa
	text = re.sub(r"\d+", " ", str(text))
	text = re.sub(r"\,", " ", str(text))
	text = re.sub(r"\?", "", str(text))
	text = re.sub(r"\.", "", str(text))
	text = re.sub(r"\!", "", str(text))
	text = text.replace(u'"', u' ')
	text = text.replace(u'️', u'')
	text = text.replace('🏻','')
	return text