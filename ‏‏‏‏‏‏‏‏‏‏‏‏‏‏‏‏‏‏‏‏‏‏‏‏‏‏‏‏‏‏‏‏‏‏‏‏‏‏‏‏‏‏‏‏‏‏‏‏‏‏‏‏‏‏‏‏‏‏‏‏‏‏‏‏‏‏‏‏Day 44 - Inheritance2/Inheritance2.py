#Inheritance2

#Use the super() Function
class MyClass:
    def __init__(self,fname,lname):
        self.FirstN = fname
        self.LastN = lname

    def PrintName(self):
        print(self.FirstN , self.LastN)

class Names(MyClass):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        #Add Properties
        self.graduationMonth=12
        self.graduationYear=year
        
    def welcom(self):
            print("Welcome ",self.FirstN,self.LastN," to class of ",self.graduationYear)
        
o = Names ("Daliah","Aljutayli",2018)
print(o.graduationMonth)
o.welcom()
