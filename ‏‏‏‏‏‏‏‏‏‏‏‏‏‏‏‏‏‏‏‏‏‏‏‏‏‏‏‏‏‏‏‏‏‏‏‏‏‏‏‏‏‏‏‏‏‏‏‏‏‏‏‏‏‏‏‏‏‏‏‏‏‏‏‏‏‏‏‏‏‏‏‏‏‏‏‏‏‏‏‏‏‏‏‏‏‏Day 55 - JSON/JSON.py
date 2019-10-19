#JSON : JSON is a syntax for storing and exchanging data

import json

#Convert from JSON to Python
j = '{"name":"Daliah","age":26,"year":2018}'
y = json.loads(j)
print("Convert from JSON to Python: ",y["age"])

#Convert from Python to JSON
x = {"name":"Daliah","age":26,"year":2018}
g = json.dumps(x)
print("Convert from Python to JSON: ",g)

#Convert Python Objects into JSON String
print( json.dumps({"name":"Daliah","age":26})  )
