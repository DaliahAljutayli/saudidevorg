# File Handling
import os
# open Modes are:
# r read .. a Append  .. w Write  .. x Create
# t Text .. b Binary  

#open File
o = open("FileName.txt" ,"r")
# Read File
print(o.read())


#open File
p = open("FileName.txt" ,"r")
# Read Part of File
print("\nRead Part of the File: ",p.read(6) )


#open File
e = open("FileName.txt" ,"r")
# Read Line of File
print("\nRead Line File: ",e.readline() )

#Write to an Existing File
n = open("FileName.txt" ,"a")
n.write("Writting New Line!")
n = open("FileName.txt" ,"r")
print(n.read())


#Close
print("\nClose File: ")
n.close()
#------------------------------
#create File
c = open("NewFile.txt","x")
c2 = open("NewFile2.txt","x")
c2.close()

#Delete
os.remove("NewFile2.txt")

   



