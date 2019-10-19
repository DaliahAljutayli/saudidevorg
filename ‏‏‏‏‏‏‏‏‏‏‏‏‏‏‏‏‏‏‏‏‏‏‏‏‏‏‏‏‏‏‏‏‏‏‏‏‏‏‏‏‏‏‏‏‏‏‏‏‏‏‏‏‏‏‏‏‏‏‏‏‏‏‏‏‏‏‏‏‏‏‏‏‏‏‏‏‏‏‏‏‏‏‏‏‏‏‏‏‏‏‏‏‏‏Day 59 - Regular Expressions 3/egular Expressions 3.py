#egular Expressions 3

import re
text = "The list contains the matches in the order they are Found"

x = re.sub("\s","--" , text)
print(x)

y = re.search("in" , text)
print("\n",y)

z = re.search(r"\bF\w+" , text)
print("\n",z.span() )

w = re.search(r"\bF\w+" , text)
print("\n",w.string )

g = re.search(r"\bF\w+" , text)
print("\n",g.group() )


 
