#Practise

# Q1: Tubles  Weekdays then convert it into String by JSON
import json
MyTuple = ("Sat","Sun","Mon","Tue","Wed","Thu","Fri")
print('The Tuple  : ',MyTuple)

convert = json.dumps(MyTuple)
print("json String:",convert)
#------------------------------
# Q2: Using Reg-Ex , write line which find word"Data" in "data is the new oil"
import re
text = "date is the new oil"
seachData = re.search("data",text)
if seachData:
   print("There is MATCH: ",seachData)
else:
   print("Not Found!")
#------------------------------   
