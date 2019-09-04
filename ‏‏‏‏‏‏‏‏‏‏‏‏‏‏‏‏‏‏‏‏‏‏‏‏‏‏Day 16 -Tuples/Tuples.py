#Tuples
#A tupleis a collection which is ordered and unchangeable

#Items
MyTuple = ("Daliah","Redna","Wafa","Amjad","Arwa")
print('The Tuple: ',MyTuple)

#Empty 
EmptyTuple = ()
print('An Empty Tuple: ',EmptyTuple)

#Items of Tuple
ItemTuple = (3,2.7,'Daliah')
print('Items of Tuple: ',ItemTuple)

#Access Tuple Items
ItemTuple = (3,2.7,'Daliah')
print('Access an Item: ',ItemTuple[2])

#Loop Through a Tuple
print('Loop of  Tuple: ',end="")
for i in MyTuple:
    print(i)

#Access Items index
print('Access by index: ',MyTuple[0:2])
