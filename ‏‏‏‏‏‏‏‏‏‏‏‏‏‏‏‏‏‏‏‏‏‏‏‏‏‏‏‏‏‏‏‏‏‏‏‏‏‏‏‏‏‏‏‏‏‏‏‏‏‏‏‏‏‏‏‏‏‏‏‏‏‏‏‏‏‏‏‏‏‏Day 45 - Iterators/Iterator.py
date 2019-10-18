#Iterator
"""
- Lists, tuples, dictionaries, and sets are all iterable Objects
- All these objects have a iter()method which used to get an iterator
"""
MyTuble = ("Apple","Banana","Cherry")
print("My Tuble: ",MyTuble)
MyIterator = iter(MyTuble)
print("\nIterator Tuble:")
print(next(MyIterator)) #Apple
print(next(MyIterator)) #Banan
print(next(MyIterator)) #Cherry

#Looping Iterator
MyName = "Daliah"
MyIterator2 = iter(MyName)
print("\nIterator String:")
for i in MyName:
    print(next(MyIterator2))

#Create an Iterator
class Numbers:
    def __iter__(self):
        self.a = 1 
        return self
    def __next__(self):
        x = self.a
        self.a +=1
        return x
MyClass = Numbers()
MyIterator3 = iter(MyClass)
print("\nIterator :")
print(next(MyIterator3))
print(next(MyIterator3))
print(next(MyIterator3)) 
#-----------------------------------------
#StopIteration
class Numbers2:
    def __iter__(self):
        self.a = 1 
        return self
    def __next__(self):
        if self.a <=10:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration       
MyClass2 = Numbers2()
MyIterator4 = iter(MyClass2)
print("\nStop Iterator at 10:")
for i in MyIterator4:
    print(i)






    
