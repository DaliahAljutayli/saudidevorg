#Function 2

# 1 Passing a List as a Parameter
def MyFunction1(MyList):
    for i in MyList:
        print(i , end=" ")
MyList = ["Daliah","Redna","Wafa","Amjad"]
MyFunction1 ( MyList ) 

#2 Return Values
def MyFunction2(num):
    return num*num
print("\nEnter a number: ")
num = int(input())
print( MyFunction2(num) )

#3 Keyword Arguments
def MyFunction3(firstName,Career):
    print ("Hi, I'm ", firstName)
MyFunction3(Career="Computer Trainer", firstName="Daliah")

#4 Arbitrary Arguments
def MyFunction4(*name):
    print ("Computer Trainer Names: " + name[1] )
MyFunction4("Daliah","Redna","Wafa","Amjad")

#5 Recursion
def Recursion(k):
    if(k > 0 ):
        result = k + Recursion (k - 1)
        print(result)
    else:
        result = 0
    return result
print("\nRecursion Example Results: ")
Recursion(4)
