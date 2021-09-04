import re

def check_phone(text):
    number = []
    text = text.split()
    number_phone = [re.compile(r'\d\d\d\d\d\d\d\d\d\d'),re.compile(r'\+\d\d\d\d\d\d\d\d\d\d'),re.compile(r'\d\d\d\d\d\d\d\d\d\d\d')]
    for j in text:
        for i in number_phone:
            phone_number = i.search(j)
            if phone_number != None:
                phone_number = phone_number.group()
                number.append(phone_number)
    return number

