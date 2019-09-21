#Conditions and Ifstatements
# if ....
print('IF: Enter 2 Numbers ')
w = input()
q = input()
if w == q: print(w,' equal ',q)
# if ... Else
print('\nIF ... Else: Enter 2 Numbers')
a = input()
c = input()
if a < c:
    print(a,' Less than ',c)
elif a > c:
    print(a,' Greater than ',c)
elif a == c:
    print(a,' eqiial ',c)
else:
    print(' "Nothing')
#AND
print('\nIf...Else with AND: Enter 3 Numbers')
h = input()
j = input()
k = input()
if h == j and j == k:
    print('Condition are True ')
else : print('Condition are False ')
#OR
print('\nIf...Else with OR: Enter 3 Numbers')
v = input()
n = input()
m = input()
if v == n or v == m:
    print('Condition are True ')
else : print('Condition are False ')
#Short Hand If
print('\nShort Hand If...Else: Enter 2 Numbers')
d = input()
f = input()
print(d,' Less than ',f) if d < f else print(d,' Greater than ',f) if d > c else print(d,' equal ',f) if d==f else print(' "Nothing')
#Nestes IF
print('\n Nested If: Enter a Number')
z = 60
if z > 10:
    print("Above 10")
    if z > 20:
        print("Above 20!")
    else:
        print("Not above 20")














