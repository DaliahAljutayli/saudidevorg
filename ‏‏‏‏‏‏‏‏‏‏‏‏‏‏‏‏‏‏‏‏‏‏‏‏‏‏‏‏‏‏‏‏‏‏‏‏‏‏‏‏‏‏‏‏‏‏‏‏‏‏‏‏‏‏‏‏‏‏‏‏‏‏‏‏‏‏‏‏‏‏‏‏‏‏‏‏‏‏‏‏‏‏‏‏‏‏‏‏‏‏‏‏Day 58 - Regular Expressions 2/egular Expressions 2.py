#egular Expressions 2 

import re
text = "The list contains the matches in the order they are found"

x = re.findall("r" , text)
print(x)

y = re.search("\s", text)
print("1st white-spase located in:",y.start())

z = re.search("Portugal", text)
print(z)

r = re.split("\s" , text)
print(r)


