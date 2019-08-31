num1 = 5
num2 = 7
text ='Please, I want {} sandwishes and {} donutes'

print('The Original String : ',text )

# 1st Method
print('The Update of String: ',text.replace("I","We").replace("a","A").format(num1,num2))

# 2nd Method
text1 = text.replace("I","We")
text2 = text1.replace("I","We")
text3 = text2.format(5,7) #(num1,num2)
print('The Update of String: ',text3 )


