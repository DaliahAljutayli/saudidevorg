#Practise
import MyModule
import datetime
#Q1:
sum = MyModule.sum(2,2)
sub = MyModule.sub(2,2)
mult =MyModule.mult(2,2)
div = MyModule.div(2,2)

print("sum:",sum)
print("sub:",sub)
print("mult:",mult)
print("div:",div)
#-----------------------------
#Q2:
dt = datetime.datetime.now()
year = dt.year
month = dt.month
day = dt.day
print("\nYear    :",year)
print("Date,Time :",dt)
print("Month     :",month)
print("Day       :",day)
#-------------------------
# A Challenge!
dCurrent = datetime.datetime.now()
C=datetime.date.today()
Y= C - datetime.timedelta(days = 1)
T= C + datetime.timedelta(days = 1)
print("\nCurrent Date   :",C)
print("Yesterday Date :",Y)
print("Tomorrow  Date :",T)





