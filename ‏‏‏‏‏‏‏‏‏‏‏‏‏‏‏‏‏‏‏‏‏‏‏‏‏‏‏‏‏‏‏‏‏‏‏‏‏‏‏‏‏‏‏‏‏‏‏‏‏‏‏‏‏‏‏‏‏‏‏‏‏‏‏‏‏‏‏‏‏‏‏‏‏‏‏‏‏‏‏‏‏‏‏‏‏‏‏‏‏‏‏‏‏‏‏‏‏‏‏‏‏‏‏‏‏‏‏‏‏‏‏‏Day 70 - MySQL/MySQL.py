# MySQL
import mysql.connector

#Create Connection .....
mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="Dalia_100",
   database="MyDatabase"   )

mycursor = mydb.cursor()  #Call


#ALTER TABLE....
#mycursor.execute("ALTER TABLE The_customer ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


mycursor.execute("SHOW COLUMNS FROM The_customer")
for x in mycursor:
   print(x)
