#Practise
#Q1 :
class Library:
   def __init__(self,shelf,book):
      self.Shelf = shelf
      self.Book = book

#Q2:
class scinece_section(Library):
   def __init__(self,shelf,book,name):
      super().__init__(shelf,book)
      self.Name=name
      
   def welcome(self):
      print(self.Shelf,self.Book,self.Name)
#-----------------------------------------
print("Q1:")
obj = Library(300,45)
print("Value of Book=",obj.Shelf,"\nShelf Numbers:",obj.Book)

print("\nQ2:")
obj = scinece_section(300,45,"Physical Books")
obj.welcome()

print("\nQ3:")
print("Change numbers of Books and Shelfs:")
#Q3: 
obj = scinece_section(205,19,"Computer Books")
obj.welcome()

