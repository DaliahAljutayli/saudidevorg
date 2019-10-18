#Array 2

#Looping Array Element
Myarray = ["Daliah","Redna","Wafa","Amjad"]

for i in Myarray:
    print(i)

#Adding Array Elements
Myarray.append("Suha")
print("After adding an element:",Myarray)

#Removing Array Elements
# 1: pop
Myarray.pop(3)
print("After removing element :",Myarray)

# 2:
Myarray.remove("Suha")
print("After removing element :",Myarray)

#Array Methods
Myarray.append("Eman")
print("\nappend Method :",Myarray)
#--------------
Myarray.sort()
print("sort Method :",Myarray)
