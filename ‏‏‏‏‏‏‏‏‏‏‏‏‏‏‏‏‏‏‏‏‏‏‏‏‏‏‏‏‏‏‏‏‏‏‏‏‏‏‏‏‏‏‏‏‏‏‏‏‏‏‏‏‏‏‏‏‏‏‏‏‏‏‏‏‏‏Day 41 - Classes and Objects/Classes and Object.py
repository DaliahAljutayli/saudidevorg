#Classe And Objects

#Create a Class
class MyClass:
    num = 5 # propert

#Create Object
O = MyClass()
print("My Class: ",O.num)

#The init Function
class MyClass2:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = MyClass2("Daliah",26)
print(p.name,p.age)

