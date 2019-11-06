#MYSQL 3

import mysql.connector

#Create Connection .....
mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="Dalia_100",
   database="DB"   )
mycursor = mydb.cursor()  #Call

#MySQL Order By....
sql="SELECT * FROM customer2 ORDER BY name"
mycursor.execute(sql)
result=mycursor.fetchall()
print("Order By:")
for i in result:
   print(i)

#ORDER BY DESC.....
sql="SELECT * FROM customer2 ORDER BY name DESC"
mycursor.execute(sql)
result=mycursor.fetchall()
print("\nOrder By DESC:")
for x in result:
   print(x)

#Delete From By....
sql="DELETE FROM customer2 WHERE address ='ArRass'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount," record(s) was Delete! \n")

#Delete From By....
sql="DROP TABLE customer2"
mycursor.execute(sql)
print("Table was Drop!")
