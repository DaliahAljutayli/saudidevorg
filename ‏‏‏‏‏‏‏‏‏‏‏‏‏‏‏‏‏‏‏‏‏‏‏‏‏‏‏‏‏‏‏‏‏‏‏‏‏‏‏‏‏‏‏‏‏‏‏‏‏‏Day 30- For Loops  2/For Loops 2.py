#Loops : For 2
MySet = ['Daliah','Redna','Wafa','Amjad','Eman']

print('MySet:',MySet,end=' ')

#The range(one parameter)Function
print('\nRange(4):')
for i in range(4):
    print(MySet[i])

#The range(Two parameters)Function
print('\nRange(0,2):')
for i in range(0,2):
    print(MySet[i])

#The range(Three parameters)Function
print('\nRange(0,3,2):')
for i in range(0,3,2):
    print(MySet[i])

#Else in For Loop
print('\nElse:')
for i in range(len(MySet)):
    print(MySet[i])
else:
    print('Finish!')

#Nested Loops
print('\nNested Loops:')
myset = ['daliah','redna','wafa','amjad','eman']
for i in MySet:
    for c in myset:
        print(i,c)
