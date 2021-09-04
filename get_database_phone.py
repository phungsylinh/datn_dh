import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="20081998",
  database="data_phone"
)
mycursor = mydb.cursor()

#mycursor.execute("SELECT First_name, Status FROM name_phone")

#myresult = mycursor.fetchall()

def get_status(name):
  mycursor.execute("SELECT Status FROM name_phone WHERE First_name = 'name'")
  myresult = mycursor.fetchall()
  return myresult[0]