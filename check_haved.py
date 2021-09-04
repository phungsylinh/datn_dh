import mysql.connector
import datetime
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="20081998",
  database="dataset"
)

mycursor = mydb.cursor()

def check_have(name_phone):
  text = "SELECT * FROM products where Name_pro = '{name}'"
  text = text.format(name = name_phone)
  mycursor.execute(text)
  myresult = mycursor.fetchall()
  if myresult[0][6] == 'Còn hàng':
    return True
  else:
    return False
def get_infor_care_phone(dics):
    text = "INSERT INTO care_product (Product,phone,email) values (%s,%s,%s)"
    values = (dics['Product'],dics['phone'],dics['email'])
    mycursor.execute(text,values)
    mydb.commit()
    return "Chúng tôi đã nhận được thông tin của bạn. Chúng tôi sẽ liên lạc với bạn ngay khi có hàng."