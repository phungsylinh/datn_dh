import mysql.connector
import datetime
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="20081998",
  database="dataset"
)

mycursor = mydb.cursor()

def check_infor(name_phone):
  infor = ""
  dics = {}
  text = "SELECT * FROM infor_product where Name_pro = '{name}'"
  text = text.format(name = name_phone)
  mycursor.execute(text)
  myresult = mycursor.fetchall()
  dics["Màn hình"] = myresult[0][2]
  dics["Kích thước màn hình"] = myresult[0][3]
  dics["Pin"] = myresult[0][4]
  dics["Màu sắc"] = myresult[0][5]
  dics["Khả năng"] = myresult[0][6]
  dics["Hãng sản xuất"] = myresult[0][7]
  dics["Quốc gia"] = myresult[0][8]
  for i in dics:
    infor += str(i) + " : " + str(dics[i]) + " ; " + "\n"
  return infor

def check_price(name_phone):
  text = "SELECT Price FROM products where Name_pro = '{name}'"
  text = text.format(name = name_phone)
  mycursor.execute(text)
  myresult = mycursor.fetchone()
  price = myresult[0]
  return price

def check_infor_buy(dics):
  if len(dics['Address']) == 0:
    return "Bạn cần cung cấp địa chỉ để phục vụ cho việc giao hàng ạ."
  elif len(dics['Number_phone']) == 0:
    return "Bạn cần cung cấp số điện thoại để thuận tiện cho việc liên lạc. Xin cảm ơn."
  elif len(dics['Product']) == 0:
    return "Chúng tôi chưa rõ bạn đang quan tâm đến sản phẩm nào ạ."
  else:
    now = datetime.datetime.utcnow()
    a = now.strftime('%Y-%m-%d %H:%M:%S')
    dics['dates'] = a
    dics['Status'] = "Đã đặt hàng"
    text = "INSERT INTO customers (Name,Address,Number_phone,Email,Product,Status,dates) values (%s,%s,%s,%s,%s,%s,%s)"
    values = (dics['Name'],dics['Address'],dics['Number_phone'],dics['Email'],dics['Product'],dics['Status'],dics['dates'])
    mycursor.execute(text,values)
    mydb.commit()
    return "Cảm ơn quý khách tin tưởng cửa hàng của chúng tôi"