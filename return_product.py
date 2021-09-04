import datetime


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="20081998",
  database="dataset"
)

mycursor = mydb.cursor()


def by_email(email):
  text = "SELECT Name,Number_phone,Product,dates FROM customers where Email = '{email}'"
  text = text.format(email = email)
  mycursor.execute(text)
  myresult = mycursor.fetchall()
  if len(myresult) == 0:
    return "Chúng tôi không tìm thấy thông tin  về email của bạn"
  else:
    x = datetime.datetime.now()
    datess = myresult[0][3]
    y = x - datess
    y = y.days
    if (y > 14 ):
      infor = "Sản phẩm của bạn mua từ {} nay đã quá 14 ngày đổi chả. Nên không thể trả lại sản phẩm."
      return infor.format(datess)
    else:
      name = myresult[0][0]
      number_phone = myresult[0][1]
      product = myresult[0][2]
      datess = myresult[0][3]
      infor = "Thông tin đơn hàng: Tên khách hàng: {name} ; sản phẩm :{product} ; số điện thoai : {number_phone} ; email : {email} ; ngày mua: {datess} ; Bạn có thể đem máy đến cửa hàng gần nhất của chúng tôi để nhân viên xem xét máy và đổi máy giúp bạn"
      infor = infor.format(name = name ,number_phone = number_phone,product=product,email=email,datess=datess)
      return infor
def by_phone(phone_number):
  text = "SELECT Name,Email,Product,dates FROM customers where Number_phone = '{phone_number}'"
  text = text.format(phone_number = phone_number)
  mycursor.execute(text)
  myresult = mycursor.fetchall()
  if len(myresult) == 0:
    return "Chúng tôi không tìm thấy thông tin  về số điện thoại của bạn"
  else:
    x = datetime.datetime.now()
    datess = myresult[0][3]
    y = x - datess
    y = y.days
    if (y > 14 ):
      infor = "Sản phẩm của bạn mua từ {} nay đã quá 14 ngày đổi chả. Nên không thể trả lại sản phẩm."
      return infor.format(datess)
    else:
      name = myresult[0][0]
      email = myresult[0][1]
      product = myresult[0][2]
      datess = myresult[0][3]
      infor = "Thông tin đơn hàng: Tên khách hàng: {name} ; sản phẩm :{product} ; số điện thoai : {number_phone} ; email : {email} ; ngày mua: {datess} ; Bạn có thể đem máy đến cửa hàng gần nhất của chúng tôi để nhân viên xem xét máy và đổi máy giúp bạn"
      infor = infor.format(name = name ,number_phone = phone_number,product=product,email=email,datess=datess)
      return infor
