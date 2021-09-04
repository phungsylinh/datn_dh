import random
import json
import torch
from model import NeuralNet
import _pickle as cPickle
from detect_ner import check_name,check_address
from process import bag_of_words,tokenizes,process_data
from sentimentanalysis import load_model
from check_mail import check_mail
from check_name_phone import check_name_phone
from check_infor import check_infor ,check_price ,check_infor_buy
from check_phone import check_phone
from textTOspeech import TextToSpeech
from return_product import by_email, by_phone
from process import tokenizes
from review import review_save
from check_haved import check_have,get_infor_care_phone
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


with open('intents.json','r',encoding = 'utf8') as f:
	intents = json.load(f)
FILE = 'data_chat.pth'
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]



model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# bot_name = "Sam"
# print("Let's chat! (type 'quit' to exit)")

# while True:
#     sentence = input('You : ');
#     if sentence == "quit":
#         break
# sentences = ["Xin chào","Sản phẩm này quá xấu","Tôi tên là Linh","Tôi sẽ lấy sản phẩm này","Bạn có thể giao hàng vào thứ bảy"
#             ,"Cảm ơn","hẹn gặp lại bạn","Có thể giảm giá không","Hello","Tôi rất thích nó"]
# tag_test = ["greeting","review","give_name","order","completeorder","thanks","goodbye","negotiate","greeting","review"]
# tagss = []
# for sentence in sentences:
#     sentence = tokenizes(sentence)
#     X = bag_of_words(sentence, all_words)
#     X = X.reshape(1, X.shape[0])
#     X = torch.from_numpy(X).to(device)

#     output = model(X)
#     _, predicted = torch.max(output, dim=1)
#     tag = tags[predicted.item()]
#     tagss.append(tag)
# print("{:100}||{:25}||{25}".format("sentence", "True", "Pred"))
# print(150 * "*")
# for w, t, pred in zip(sentences, tag_test, tagss):
#     print("{:100}: {:25} : {25}".format(w, t, pred))
    # probs = torch.softmax(output, dim=1)
    # prob = probs[0][predicted.item()]
    # if prob.item() > 0.75:
    #     for intent in intents['intents']:
    #         if tag == intent["tag"]:
    #         	if tag == 'give_name':
    #         		name = check_name(sentence)
    #         		respon = random.choice(intent['responses'])
    #         		respon = respon.replace("name",name)
    #         		print(f"{bot_name}:{respon}")
    #         	else:
    #             	print(f"{bot_name}:{random.choice(intent['responses'])}")
    # else:
    #     print(f"{bot_name}: I do not understand...")
count_tags = []
care_pro = {
    "Product" : "",
    "phone"   : "",
    "email"   : ""
}
reviews = {
    "Product":"",
    "Review" : "",
    "Assess" : "",
    "dates":""
}
customer = {
    "Name":"",
    "Address":"",
    "Number_phone":"",
    "Email":"",
    "Product":"",
    "Status":"",
    "dates":""
}
with open('model_chat.pkl', 'rb') as fid:
    model_chat = cPickle.load(fid)
with open('tf_chat.pkl', 'rb') as fid:
    tf_chat = cPickle.load(fid)
def get_response(sentence):
    while True:
        if sentence == "quit":
            respon = "Chào tạm biệt bạn 😃 "
            return respon
            #break
            
        #Kiểm tra email
        email = check_mail(sentence)
        if len(email)!= 0 :
            for i in email:
                sentence = sentence.replace(i,"email_address")
                customer['Email'] = i
                care_pro['email'] = i
        else :
            sentence = sentence

        #Kiểm tra số điện thoại
        phone_number = check_phone(sentence)
        if(len(phone_number) != 0):
            for i in phone_number:
                sentence = sentence.replace(i,"phone_number")
                customer['Number_phone'] = i
                care_pro['phone'] = i
        else:
            sentence = sentence

        #Kiểm tra điện tên điện thoại
        name_phone = check_name_phone(sentence)
        if len(name_phone) != 0 :
            a = check_have(name_phone[0])
            for i  in name_phone:
                sentence = sentence.replace(i,"product")
                customer['Product'] = i
                reviews['Product'] = i
                care_pro['Product'] = i
        else:
            sentence = sentence

        #Kiểm tra tên người dùng
        name = [check_name(sentence)]
        if len(name[0]) != 0:
            sentence = sentence.replace(name[0],"name")
            customer['Name'] = name[0]
        else:
            sentence = sentence

        address = check_address(sentence)
        if len(address) != 0:
            sentence = tokenizes(sentence)
            sentence = ' '.join(sentence)
            for i in address:
                sentence = sentence.replace(i,"address")
            address = ' '.join(address)
            customer['Address'] = address

        # sentences = sentence
        # sentence = sentence.lower()
        # sentence = process_data(sentence)

        # sentence = tf_chat.transform([sentence])

        # tag = model_chat.predict(sentence)
        # tag = tag[0]
        sentences = sentence
        sentence = tokenizes(sentences)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]

        if prob.item() > 0.70:
        # if max(model_chat.predict_proba(sentence)[0]) >= 0.4:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    count_tags.append(tag)
                    if tag == 'give_name':
                        respon = random.choice(intent['responses'])
                        respon = respon.replace("name",name[0])
                        #print(f"{bot_name}:{respon}")
                    elif tag == 'review':
                        review = load_model.give_review([sentences])
                        reviews['Review'] = sentences
                        if len(reviews['Product']) != 0:
                            if review == 'negative':
                                reviews['Assess'] = 'negative'
                                review_save(reviews)
                                respon = random.choice(intent['responses'][0])
                            else:
                                reviews['Assess'] = 'positive'
                                review_save(reviews)
                                respon = random.choice(intent['responses'][1])
                        elif review == 'negative':
                            respon = random.choice(intent['responses'][0])
                        else:
                            respon = random.choice(intent['responses'][1])
                    elif tag == "infor_product":
                        if(len(name_phone) != 0):
                            product = name_phone[0]
                            information = check_infor(product)
                            price = check_price(product)
                            respon = random.choice(intent['responses'])
                            respon = respon.replace("product",product)
                            respon = respon.replace("information",information)
                            respon = respon.replace("price",price)
                            if(not a):
                                respon = respon + ". Xin lỗi quý khách sản phẩm này bên chúng tôi đang tạm thời hết hàng ạ. Bạn có thể để lại thông tin để chúng tôi có thể báo cho bạn khi có hàng được không ạ."
                        else:
                            respon = "Xin lỗi quý khách. Chúng tôi hiện không có sản phẩm này."
                    elif tag == "get_contact":
                        if len(count_tags) > 2 :
                            if count_tags[-2] == "returns" and (len(phone_number) != 0 or len(email) != 0 ) :
                                if len(phone_number) != 0:
                                    respon = by_phone(phone_number[0])
                                else:
                                    respon = by_email(email[0])
                            elif count_tags[-2] == "order" or (count_tags[-3] == "order" and count_tags[-2] == "address"):
                                respon = check_infor_buy(customer)
                            elif len(phone_number) == 0 and len(email) == 0:
                                respon = "Chúng tôi vẫn chưa nhận được thông tin của bạn. Bạn vui lòng cung cấp lại thông tin"
                            else:
                                respon = random.choice(intent['responses'])
                        elif (count_tags[-2] == "infor_product" and (len(phone_number) != 0 or len(email) != 0 ) and (not check_have(care_pro['Product']))):
                            respon = get_infor_care_phone(care_pro)
                        else:
                            respon = random.choice(intent['responses'])
                    elif tag == "order":
                        respon = check_infor_buy(customer)
                    elif tag == "address":
                        if count_tags[-2] == "order":
                            respon = check_infor_buy(customer)
                        else:
                            respon = random.choice(intent['responses'])
                    else:
                        respon = random.choice(intent['responses'])
                            #print(f"{bot_name}:{random.choice(intent['responses'])}")
        else:
             respon = "Tôi không hiểu bạn đang nói gì bạn có thể nói rõ lại được không"
            #print(f"{bot_name}: I do not understand...")
        #TextToSpeech(respon)
        return respon