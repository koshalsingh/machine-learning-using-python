factors=[]
num= int(input('enter the number'))
for i in range(1, num+1):
    if(num%i==0):
        factors.append(i)
print('factors of ', num ,'are', factors)
