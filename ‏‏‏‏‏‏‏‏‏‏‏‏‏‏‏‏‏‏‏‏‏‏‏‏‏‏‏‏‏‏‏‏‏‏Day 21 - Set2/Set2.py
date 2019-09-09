#Sets 2

MySet = {'Daliah','Redna','Eman','Wafa','Amjad','Maha','Fai'}
print('My Set   : ',MySet)

#Lenght
print('Lenght of My Set: ',len(MySet) )

#Constructor
Constructor = set( ('Shyma','Uroab','Hessah') )
print('Constructor: ',Constructor ) 


#Remove Item
# 1st Method:
MySet.remove('Maha')
print('Removing Item: ',MySet)

# 2nd Method:
MySet.discard('Eman')
print('Discare Item: ',MySet)

# 3rd Method:
MySet.pop()
print('Pop Item: ',MySet)

# 4th Method:
MySet.clear()
print('Clear All Items: ',MySet)

# 5th Method:
del MySet
print('Delete Set: ',MySet)

