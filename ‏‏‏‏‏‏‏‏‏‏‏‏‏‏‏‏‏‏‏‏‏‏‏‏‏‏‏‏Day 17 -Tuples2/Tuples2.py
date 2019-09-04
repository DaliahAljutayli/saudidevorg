# Tuples2
#Items
MyTuple = ("Daliah","Redna","Wafa","Amjad","Arwa")
print('My Tuple: ',MyTuple)

#Check if Item Exists
print("Is Daliah Exists")
if 'Daliah' in MyTuple:
    print('Yes,it exist')

#Repeat Item
TheTuple = ('Daliah')*3
print('Repeat Item: ',TheTuple)


# + Operator in Tuple
MyTuple2 = ("Daliah","Redna","Wafa","Amjad","Arwa")
AllTuples = MyTuple + MyTuple2
print('All Tuple: ',AllTuples)

#Tuple Length
print('The Length of Tuple: ',len(MyTuple))

#The tuple()Constructor
Tuples = tuple(( 'Daliah','Redna','Wafa' )) #Double Brackets
print('Constructor: ',Tuples)
