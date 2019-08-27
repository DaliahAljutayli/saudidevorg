#String Format

#Combine strings and numbers by using the format()
# To Combain we add numbert to String by {}
Number = 2019
Text = "We combine strings with {}"
print( Text.format(Number) )

#Unlimited number of arguments
a = 1414
b = 2019
Text = "Unlimited number of arguments Like {} , Hello {}"
print( Text.format(a,b) )

#Index numbers to be sure the arguments
a = 1   #0
b = 3   #1
c = 2   #2
Cheer = "{0} , {1} , {2} ...... Gooooo"
print(Cheer.format(a,c,b))

