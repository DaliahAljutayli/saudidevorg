#Classes and Objects 2

#Object Method
class MyClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def MyFunc(self):
        print("My name is ",self.name , " age: ",self.age)

o = MyClass("Daliah",25)
o.MyFunc()

#Modify Object Properties
o.age = 26
print("Modify Properties ",o.age)

#Delete Object
del o
print("After Deletting Object ",o)
