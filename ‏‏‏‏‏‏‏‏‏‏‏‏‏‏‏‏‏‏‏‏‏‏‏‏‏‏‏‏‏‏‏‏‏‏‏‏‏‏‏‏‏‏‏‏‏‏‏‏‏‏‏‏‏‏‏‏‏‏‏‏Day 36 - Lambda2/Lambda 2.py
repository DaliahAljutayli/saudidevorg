# Lambda2 

#Takes one argument,
def Myfunc(n):
    return lambda a: a*n

num = Myfunc(2)
print( num(11) )

#Take two argument
def Myfunc2(n):
    return lambda a: a*n

num = Myfunc2(2)
num = Myfunc2(3)

print( num(11) , num(22) )

