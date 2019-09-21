#Practise

List = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

print('Odd: ')
for A in range(3,18):
    if A %2 ==1:
        print(A ,end=' ')

print('\nEven: ')
for A in range(2,18):
    if A %2 ==0:
        print(A ,end=' ')


a = [2,4,6,8,10,12,14,16]
b = [3,5,7,9,11,13,15,17]
for i in a:
    for j in b:
        print(i,'-',j)
