import re
from replace_file import replace
from pyvi import ViTokenizer

def read_data(path_data):
    read = open(path_data,'r',encoding = 'utf-8')
    read = read.readlines()
    data = [i.replace("\n","") for i in read]
    return data

def process_data(text):
	text = text.lower()
	text = re.sub(r"\b[a-zA-Z]\b", "", str(text))
	for i, j in replace.items():
        text = text.replace(i, j)
	text = re.sub(r'(.)\1+', r'\1', text) #Chuyển nhiều hơn 1 chữu về 1 chữ
	text = re.sub(r"\s+", " ", str(text)) #Chuyển nhiều khoảng trắng về 1 khoảng trắng
	text = ViTokenizer.tokenize(text)
    texts = text.split()
    texts = [t.replace('_', ' ') for t in texts]
    len_text = len(texts)
    for i in range(len_text):
        cp_text = texts[i]
        if cp_text in not_list: # Xử lý vấn đề phủ định (VD: không xấu--> notnag)
            numb_word = 2 if len_text - i - 1 >= 4 else len_text - i - 1

            for j in range(numb_word):
                if texts[i + j + 1] in pos_list:
                    texts[i] = 'notpos'
                    texts[i + j + 1] = ''

                if texts[i + j + 1] in nag_list:
                    texts[i] = 'notnag'
                    texts[i + j + 1] = ''
        # else: #Thêm feature cho những sentiment words (vd tốt--> tốt positive)
        #     if cp_text in pos_list:
        #         texts.append('positive')
        #     elif cp_text in nag_list:
        #         texts.append('nagative')

    text = u' '.join(texts)
    # xóa ký tự thừa
    text = text.replace(u'"', u' ')
    text = text.replace(u'️', u'')
    text = text.replace('🏻','')
    return text


    