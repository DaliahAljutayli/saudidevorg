#Dictionaries
#A dictionary is a collection which is unordered,
#changeable and indexed.

dictionary = {
  "Name": 'Daliah',
  "Age" : 26 ,
  "Career": "Computer"  
    }
print('My Dictionary is: ',dictionary)

#Accessing Items
print('My Name is ... ',dictionary["Name"] )

#Accessing Items
print('My age is ... ',dictionary.get("Age") )

#Change Values
dictionary["Career"] = "Computer Trainer"
print('Change Value: ',dictionary)

#Loop Through a Dictionary
print('  Keys are   : ',end=" ")
for i in dictionary:
    print(i,end=" ")
 4
print('\n1-Values are : ',end=" ")
for i in dictionary:
    print(dictionary[i],end=" ")

print('\n2-Values are : ',end=" ")
for i in dictionary.values():
    print(i,end=" ")

print('\n3-Values are : ')
for i,o in dictionary.items():
    print(i,o)
