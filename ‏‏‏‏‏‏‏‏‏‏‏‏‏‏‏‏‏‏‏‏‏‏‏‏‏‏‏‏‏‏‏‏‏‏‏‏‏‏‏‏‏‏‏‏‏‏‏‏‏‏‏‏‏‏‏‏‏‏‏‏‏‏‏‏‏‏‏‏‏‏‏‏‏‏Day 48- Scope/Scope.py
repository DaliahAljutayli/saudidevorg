#Scope

#Local Scope
def MyFunc():
   num = 403
   print("Local Scope: ",num)

MyFunc() #class function
#-----------------------------
#Function inside Function
def OutsideFunc():
   num = 90
   def insideFunc():
      print("From Inside Function: ",num)
   insideFunc()

OutsideFunc() 
#--------------------------------
#Global Scope
GlobalNum = 300
def Func():
   print("Global Scope: ",GlobalNum)

Func()
