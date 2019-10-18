#Modules 2

#Re-naming a Module
import mymodule as PersonalMod
a = PersonalMod.person["year"]
print(a,"\n")
#------------------------
#Import From Module
from mm import person
print(person["name"],"\n")
#------------------------
#Built-in
import platform
x = platform.system()
print(x,"\n")

#Using dir()
y = dir(platform)
print(y)



