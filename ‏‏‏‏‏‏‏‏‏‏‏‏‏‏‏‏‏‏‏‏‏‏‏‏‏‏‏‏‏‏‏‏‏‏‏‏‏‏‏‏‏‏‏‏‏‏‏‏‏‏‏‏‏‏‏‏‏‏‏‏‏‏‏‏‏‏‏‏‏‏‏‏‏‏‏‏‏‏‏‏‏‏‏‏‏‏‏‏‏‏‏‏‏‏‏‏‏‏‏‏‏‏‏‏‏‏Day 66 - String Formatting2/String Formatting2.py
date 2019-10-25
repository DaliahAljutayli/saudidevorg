# String Formatting2 :

# Index Numbers:
item = 567
q = 3
price = 49

txt3 = "I wan {1} pieces of item number {0} for {2:.2f} SRs"
print(txt3.format(item,q,price))

#-----------------------
age = 26
name = "Daliah"
t = "My name is {1} , My MUM named me {1} ,I'm {0} years old"
print(t.format(age,name))

#-----------------------
#Named Indexes:
text = "My name is {n} , My MUM named me {n} ,I'm {a} years old"
print(text.format(a=26,n="Daliah"))
