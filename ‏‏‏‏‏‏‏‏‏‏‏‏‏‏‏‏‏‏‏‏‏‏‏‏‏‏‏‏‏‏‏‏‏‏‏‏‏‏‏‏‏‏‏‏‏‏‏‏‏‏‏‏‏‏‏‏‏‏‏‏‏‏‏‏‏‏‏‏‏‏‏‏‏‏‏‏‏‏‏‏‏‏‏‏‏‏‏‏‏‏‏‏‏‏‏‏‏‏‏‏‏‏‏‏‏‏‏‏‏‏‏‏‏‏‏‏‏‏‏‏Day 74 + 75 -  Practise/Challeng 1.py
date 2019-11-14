#Practise

import os
# Q1: Write a text into MyFile.txt then Print
opn = open("MyFile.txt" ,"a")
opn.write("The best way we learn anything is by practice and exercise questions")

opn = open("MyFile.txt" ,"r")
print("After Adding:\n")

print(opn.read())

#opn.close()
