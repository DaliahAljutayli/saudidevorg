#Scope2 

#Naming Variables
num = 500 #Global

def MyFun():
   num = 300 #Local
   print("inside fun: ",num)

MyFun()
print("outside fun:",num)
#---------------------------
#Global Keyword
def GFun():
   global num
   num = 98

GFun()
print("\n",num)
