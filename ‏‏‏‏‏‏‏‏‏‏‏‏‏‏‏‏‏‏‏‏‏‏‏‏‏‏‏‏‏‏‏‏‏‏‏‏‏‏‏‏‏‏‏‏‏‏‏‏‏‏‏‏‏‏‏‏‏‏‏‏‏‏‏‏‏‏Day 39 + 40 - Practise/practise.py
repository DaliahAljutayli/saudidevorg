#Practise

# Q1: Use Recursion of 5^3
def Recursion(num):
    return num*num*num
print("5^3 =",Recursion(5))
#-------------------------------------------
# Q2: Create List , call lamdba which print event number only
MyList = [-4,-6,-5,-1,2,3,7,9,88]
x = lambda a : a if a>0 else None
for i in MyList:
    if(x(i))!= None: print(x(i),end=" ")
