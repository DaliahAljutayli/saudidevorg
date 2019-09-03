#Lists 2

#Using List Index
MyList = ['Samer','Redna','Wafa','Daliah','Amjad','Arwa']
print('Computer Trainers are: ',MyList[1:4])

#Check if Item Exists
MyList = ['Samer','Redna','Wafa','Daliah','Amjad','Arwa']
print('Is Daliah in the List? ',end=" ")
if 'Daliah' in MyList:
    print('Yes,She is.')

#Repeat Item in List
print('Repeat Item in List ',(MyList[3]*2))

#+ Operator in List
MyList = ['Redna','Wafa','Daliah','Amjad']
NewList= ['Ashwaq','Suha','Eman']
print('Merge 2 Lists: ',(MyList+NewList))
