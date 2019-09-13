#Practice 
# Q1: add 4,8,12 to set={1,3,5,7,8} ....then Delete 8 after that clear the whole set
MySet={1,3,5,7,8}
print('My Set: ',MySet)

MySet.update( [1,3,5,7,8,4,8,12] )
print('Update My Set: ',MySet)

MySet.remove(8)
print('Removing 8 from Set: ',MySet)

MySet.clear()
print('Clearing Set: ',MySet)

print('-----------------------------')

# Q2: Create an dictionary then add an values
dictionary = {
'Name': "Pigeon",
"Type":"Bird",
"Skin Cover" : "feathers"   }
print(" Dictionary Items: ",dictionary)

print("The \'Type\' Value : ",dictionary["Type"])

dictionary["Skin Cover"] ="Colorfull feathers"
print("Change Skin Cover: ", dictionary)

