#Practise
import mysql.connector
mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="Dalia_100",
   database="MyEmployee")
c = mydb.cursor() #call

# Q2-1: Display/Show the table content?
sql = "SELECT * FROM Employee"
c.execute(sql)
result = c.fetchall()
for i in result:
   print(i)
   
print("\n")#-------------------------------------------

# Q2-2: Display/Show First Name, Gender and Salary columns?
sql = "SELECT FirstName,Gender,Salary FROM Employee"
c.execute(sql)
result = c.fetchall()
for x in result:
   print(x)

print("\n")#-------------------------------------------

# Q2-3: Display/Show ALL content DESC Order by name?
sql = "SELECT * FROM Employee ORDER BY FirstName DESC"
c.execute(sql)
result = c.fetchall()
for t in result:
   print(t)

print("\n")#-------------------------------------------

# Q2-4: Delete Row/Record which age = 34 ?
sql = "DELETE FROM Employee WHERE Age = 34"
c.execute(sql)
mydb.commit()
print(c.rowcount, "record(s) was deleted!\n")
sql = "SELECT * FROM Employee"
c.execute(sql)
result = c.fetchall()
for y in result:
   print(y)
