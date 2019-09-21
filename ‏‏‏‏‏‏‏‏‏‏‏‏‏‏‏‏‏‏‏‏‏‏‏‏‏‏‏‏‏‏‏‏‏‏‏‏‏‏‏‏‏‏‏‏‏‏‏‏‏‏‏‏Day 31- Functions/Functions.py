#Functions
""" A functionis a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A functioncan return data as a result """

# 1: 
#Creating a Function
def FunctionName():
    print('Hellow from a Function')
#Calling a Function
FunctionName()


# 2: 
def FunName(name):
     print(name + ' Welcom to the Function') 
#Parameters
print('\nEnter Your Name:',end='')
FunName( name = input() )

# 3:
#Default Parameter Value
def FName(name = ''):
     print(name + ' as Default Value') 
#Parameters
print('\nDefault Parameter Value: ')
FName('Daliah')
FName()
FName('Redna')

