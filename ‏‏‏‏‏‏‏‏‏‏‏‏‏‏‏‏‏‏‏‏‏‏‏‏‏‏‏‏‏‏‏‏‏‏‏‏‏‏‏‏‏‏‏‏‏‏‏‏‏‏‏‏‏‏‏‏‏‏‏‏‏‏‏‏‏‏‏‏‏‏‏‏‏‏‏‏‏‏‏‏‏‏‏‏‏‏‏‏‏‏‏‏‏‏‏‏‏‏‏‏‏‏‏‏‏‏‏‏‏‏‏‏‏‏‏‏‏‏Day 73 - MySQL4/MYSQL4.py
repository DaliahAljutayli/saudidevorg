#MYSQL 4 
import mysql.connector
mydb=mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="Dalia_100",
   database="DB")

mycursor=mydb.cursor()

#UPdate.....
sql="UPDATE customer2 SET name='Redna' WHERE name='Dali' "
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount," record(s) Updated!")

#Limit....
mycursor.execute("SELECT * FROM customer2 LIMIT 2")
result=mycursor.fetchall()
for i in result:
   print(i)

#Start from Other Position...
mycursor.execute("SELECT * FROM customer2 LIMIT 2 OFFSET 2")
re=mycursor.fetchall()
for x in re:
   print(x)

