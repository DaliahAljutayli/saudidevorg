#JSON2

import json

#Format the result
x = {"name":"Daliah","age":26,"year":2018}

print(json.dumps(x,indent=2)) #مسافة بادئة=2

print("\n\n",json.dumps(x,indent=2 , separators=(".","-"))) # تغيير الفواصل

#Order the result
print("\n\n",json.dumps(x,indent=3 ,sort_keys=True) ) 
