#Dictionaries 2

dictionary = {
  "Name": 'Daliah',
  "Age" : 26 ,
  "Year" : 1993,
  "Graduate_Year" : 2018,
  "Career": "Computer"  
    }
print('My Dictionary is: ',dictionary)

#Check if Key Exists
print('Is Name key in the dictionary?')
if 'Name' in dictionary:
    print('Yes,it\'s inside dictionary')

#Dictionary Length
print('Dictionary Length= ',len(dictionary) )

#Adding Items
dictionary['Major'] = 'IT'
print('After Adding Item : ',dictionary)

#Removing Items
# 1st Method:  Select a key to remove
dictionary.pop('Career')
print('After Removing Key: ',dictionary)

# 2nd Method:  Remove last Item
dictionary.popitem()
print('Removing Last Key : ',dictionary)

# 3rd Method: Empties the dictionary
dictionary.clear()
print('Empties the dictionary: ',dictionary)

# 4th Method: Delete the dictionary completely
dictionary2 = {"Name": 'Daliah',"Age" : 26 ,"Year" : 1993,
               "Graduate_Year" : 2018,"Career": "Computer" }
del dictionary2
print('Delete the dictionary completely : ',dictionary2)







