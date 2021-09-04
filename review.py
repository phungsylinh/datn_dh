import mysql.connector
import datetime
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="20081998",
  database="dataset"
)
mycursor = mydb.cursor()

def review_save(dics):
    now = datetime.datetime.utcnow()
    a = now.strftime('%Y-%m-%d %H:%M:%S')
    dics['dates'] = a
    text = "INSERT INTO review (Product,Review,Assess,dates) values (%s,%s,%s,%s)"
    values = (dics['Product'],dics['Review'],dics['Assess'],dics['dates'])
    mycursor.execute(text,values)
    mydb.commit()