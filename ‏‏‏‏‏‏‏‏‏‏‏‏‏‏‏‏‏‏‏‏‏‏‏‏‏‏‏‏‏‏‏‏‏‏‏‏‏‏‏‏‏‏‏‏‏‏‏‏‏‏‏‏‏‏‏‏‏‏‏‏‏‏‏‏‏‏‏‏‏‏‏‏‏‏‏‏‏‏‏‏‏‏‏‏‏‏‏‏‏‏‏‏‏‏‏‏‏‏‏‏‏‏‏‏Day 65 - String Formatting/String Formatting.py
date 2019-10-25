# String Formatting:

#one Value:
price = 49

txt1 = "The price is {} SR"
print(txt1.format(price))

txt2 = "The price is {:.2f} SR"
print(txt2.format(price))

# Multiple Values:
item = 567
q = 3
txt3 = "I wan {} pieces of item number {} for {:.2f} SR"
print(txt3.format(q,item,price))
