#List

a = []
print('Empty List  :',a)

b = [1,3,5,6]
print('Number List :',b)

c = ['Daliah','Redna','Wafa']
print('String List :',c)

e = ['Daliah','Redna','Wafa',1,2,3]
print('Complex List:',e) 


f = ['Redna','Daliah','Wafa',1,2,3]
print('Access Items:',f[1])

#Loop Through a List 
d =['Redna','Daliah','Wafa',1,2,3]
print('Loop of List:',end=' ')
for i in d:
    print( i, end=' ')

#Change Item Value
g =['Redna','Daliah','Wafa',1,2,3]
g [3] = 'Amjad'
print('\nChange Value:',g)

#Delete Item Value
h =['Redna','Daliah','Wafa','Amjad',2,3]
del h [4]
print('Change Value:',h)
