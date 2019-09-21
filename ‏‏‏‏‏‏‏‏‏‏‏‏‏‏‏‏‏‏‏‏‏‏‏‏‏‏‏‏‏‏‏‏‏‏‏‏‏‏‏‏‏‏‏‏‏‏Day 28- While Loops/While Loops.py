#Loops : While

MySet = [1,2,3,4,5,6]
i = 0
print("Looping My Set: ")
while i < len(MySet):
    print(MySet[i])
    i+=1

# Using Break
i = 0
print("Break: ")
while i < len(MySet):
    print(MySet[i])
    if MySet[i] == 4:
        break
    i+=1

#continue Statement
i = 0
print("Continue: ")
while i < 6:
    i+=1
    if i == 3:
        continue
    print(i)

#The else Statement
i = 0
print("nElse: ")
while i < len(MySet):
    print(MySet[i])
    i+=1
else:
    print('\ni no longer less than The Set Length')
    
