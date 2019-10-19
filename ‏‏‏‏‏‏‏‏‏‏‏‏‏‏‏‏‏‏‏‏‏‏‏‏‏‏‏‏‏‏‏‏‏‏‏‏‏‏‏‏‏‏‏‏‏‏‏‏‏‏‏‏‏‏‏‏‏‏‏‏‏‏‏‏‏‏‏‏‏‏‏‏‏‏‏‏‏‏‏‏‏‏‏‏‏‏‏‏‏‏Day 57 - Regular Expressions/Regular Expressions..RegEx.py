#Regular Expressions....RegEx

import re
text = "The rain in KSA , So beautifull weather"

rx = re.search("^The.*KSA$",text )
if (rx):
   print("There is MATCH!")
else:
   print("NO MATCH")

#Special Sequences
rs = re.findall("[a-g]", text)
print(rs)
