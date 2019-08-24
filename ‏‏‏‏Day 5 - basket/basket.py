#basket: Separate String apple, orange, Limon in different ways
#1st Solution: Space inside value
x='apple '
y ='orange '
z='limon '
basket = x+y+z
print('Solution 1: '+basket)

#2nd Solution: Space as variable
x='apple'
y ='orange'
z='limon'
s=' '
basket = x+s+y+s+z
print('Solution 2: '+basket)

#3rd Solution: Use split() Function
x='apple '
y ='orange '
z='limon '
basket = x+y+z
print('Solution 3 Use split() : ',basket.split(","))

#4th Solution: Use len() Function
i = 0
input = ['apple','orange','limon'] #list
index = len(input)-1
print('Solution  Use len():',end=" ") #print string without newline
while i <= index:
    basket = input[i]
    print(basket,end=",") #print list without newline
    i+=1






