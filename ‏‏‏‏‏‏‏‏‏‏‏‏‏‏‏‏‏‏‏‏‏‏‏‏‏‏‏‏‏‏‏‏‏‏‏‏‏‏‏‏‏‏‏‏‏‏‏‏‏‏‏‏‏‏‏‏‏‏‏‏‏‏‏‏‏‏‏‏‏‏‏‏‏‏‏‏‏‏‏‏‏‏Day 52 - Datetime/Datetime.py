#Datetime

import datetime #display the current date.

#Dates
dt = datetime.datetime.now()
print("Datetime: ",dt)
#--------------------
#Creating Date Objects
d = datetime.datetime(2020,5,17)
print("Date Objects: ",d)
#--------------------
#Date Output
print("\nDatetime year: ",dt.year) #A:full Weekday
print("\nDatetime strftime Long : ",dt.strftime("%A")) #A:full Weekday
print("\nDatetime strftime Short: ",dt.strftime("%b")) #A:short Weekday
#--------------------
#The strftime() Method : formatting date objects
print("\nDatetime strftime Long : ",dt.strftime("%B")) #B: full Month name
print("Datetime strftime Short: ",dt.strftime("%b")) #B: short Month name
#--------------------


