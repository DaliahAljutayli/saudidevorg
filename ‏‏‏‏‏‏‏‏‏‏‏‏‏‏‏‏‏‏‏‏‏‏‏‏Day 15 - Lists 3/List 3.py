#Lists 3
MyList = ['Samer','Redna','Wafa','Daliah','Amjad','Arwa']
print('My List: ',MyList)
print('_______________________________________________')
#List Length
print('Length of The List: ' ,len(MyList))

#make a new list
NewList = list(('This','is','New','List'))
print("Making a New List: ",NewList)

#Add Items
MyList.append('Fatimah')
print('After Adding Item : ' ,MyList)

#add an item at the specified index
MyList.insert(0,'Maha')
print('At Specified index: ' ,MyList)

#Copy a List
# 1st Way
MyList_Copy = MyList.copy()
print('1- Copy of MyList: ' ,MyList)
# 12nd Way
MyList_List = list(MyList)
print('2- Copy of MyList: ' ,MyList_List)

#Sort the List
print('Sorting The Lsit: ' ,MyList.sort())

#Remove Item
# 1st Method: 
MyList.remove('Arwa')  #Remove "Arwa" 
print('1-Removing an item: ' ,MyList)
# 2nd Method: 
MyList.pop() #Remove Last Item
print('2-Remove Last Item: ' ,MyList)
# 3rd Method: 
MyList.clear() #Remove Last Item
print('3-Remove All Items: ' ,MyList)

