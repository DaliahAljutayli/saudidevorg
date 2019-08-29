#Operators2

#Logical Operators
x = 3
y = 6
print("AND Operators: ",x," < 5 and ",y," < 10 = ",(x<5 and y<10))
print(" OR Operators: ",x," < 5  or ",y," < 10 = ",(x<5 or y<10))
print("NOT Operators: not(",x,"<5 and ",y,"<10)= ",not(x<5 and y<10))
print("NOT Operators: not(",x,"<5  or ",y,"<10)= ",not(x>5 or y<10))
print("------------")

#Identity Operators
a = 6
b = 4
c = 4.0
listA = ['Daliah','Samer']
listB = ['Hessah','Ashwaq']

print("a is b:", (a is b) )
print("a is a:", (a is a) )
print("a is c:", (a is c) )
print("------------")
print("a is not b:", (a is not b) )
print("a is not a:", (a is not a) )
print("a is not c:", (a is not c) )
print("listA is  listB:", (listA is listB) )
print("------------")

#Membership Operators
print("Daliah in  listA:", ('Daliah' in listA) )
print("Daliah in  listB:", ('Daliah' in listB) )
print("Daliah not in  listA:", ('Daliah' not in listA) )
print("Daliah not in  listB:", ('Daliah' not in listB) )
