#Inheritance

#Create a Parent Class
class MyClass:
    def __init__(self,fname,lname):
        self.FirstN = fname
        self.LastN = lname

    def PrintName(self):
        print(self.FirstN , self.LastN)


#Create a Child Class
#Add the __init__() Function
class Names(MyClass):
    def __init__(self,fname,lname):
        MyClass.__init__(self,fname,lname)

o = Names ("Daliah","Aljutayli")
o.PrintName()

