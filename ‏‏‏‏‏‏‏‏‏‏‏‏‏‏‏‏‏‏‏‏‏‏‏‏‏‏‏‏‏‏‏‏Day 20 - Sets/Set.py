#Sets
#A setis a collection which is unordered and unindexed

#Empty Set.
MySet = {}
print('Empty Set: ',MySet)

#Create a Set.
MySet = {'Daliah','Redna','Wafa','Amjad'}
print('My Set   : ',MySet)

#Access Items
print('Items of Set: ')
for i in MySet:
    print(i ,end=' ')

#Check
print('\nIs Daliah in My Set in Set? ...', "Daliah" in  MySet)

#Add Items
MySet.add('Maha')
print(MySet)

#Update Items
MySet.update(['Daliah','Redna','Wafa','Amjad','Noura'])
print('After Updating: ',MySet)
