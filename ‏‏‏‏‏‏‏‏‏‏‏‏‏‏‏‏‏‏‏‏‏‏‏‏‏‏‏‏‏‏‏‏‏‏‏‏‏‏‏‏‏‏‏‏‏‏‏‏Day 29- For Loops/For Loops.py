# Loops 2 : For

MySet = ['Daliah','Redna','Wafa','Amjad']

print('Looping My Set:')
for i in MySet:
    print(i)

#Looping Through a String
print('\nLooping Through a String:')
for i in 'Daliah':
    print(i)

#The break Statement
print('\nBreak:')
for i in MySet:
    print(i)
    if i == 'Redna':
        break

#The continue Statement
print('\nContinue:')
for i in MySet:
    if i == 'Redna':
        continue
    print(i)
