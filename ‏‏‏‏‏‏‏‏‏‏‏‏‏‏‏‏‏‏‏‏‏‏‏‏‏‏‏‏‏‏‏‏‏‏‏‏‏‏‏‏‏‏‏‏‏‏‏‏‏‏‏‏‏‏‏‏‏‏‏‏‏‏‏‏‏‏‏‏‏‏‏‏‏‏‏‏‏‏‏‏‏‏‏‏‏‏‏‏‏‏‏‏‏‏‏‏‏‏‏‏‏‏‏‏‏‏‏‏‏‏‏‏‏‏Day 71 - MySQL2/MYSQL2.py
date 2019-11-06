# MySQL Part2 
import mysql.connector

#Create Connection .....
mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="Dalia_100",
   database="MyDatabase"   )
mycursor = mydb.cursor()  #Call


mycursor.execute("SELECT * FROM customer")
result = mycursor.fetchall()
print("Select All")
for i in result:
   print(i)
#__________________________
mycursor.execute("SELECT name,address FROM customer")
result = mycursor.fetchall()
print("\n Select Column")
for x in result:
   print(x)
#__________________________
mycursor.execute("SELECT * FROM customer WHERE name Like 'Da%'")
result = mycursor.fetchall()
print("\n Like:")
for x in result:
   print(x)
#-----------------------------------------------------------
mycursor.execute("SELECT * FROM customer")
result = mycursor.fetchone()
print("\n fetchone: ",result)
#-----------------------------------------------------------
#sql="SELECT * FROM customer WHERE name='Daliah'"
#mycursor.execute(sql)
#Tresult = mycursor.fetchall()
#print("\n")
#for y in Tresult:
 #  print(y)
#-----------------------------------------------------------

