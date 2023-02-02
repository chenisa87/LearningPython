num1 = eval(input(""))
num2 = eval(input(""))
Max = max(num1,num2)
Min = min(num1,num2)
for i in range(1,Max+1):
    if Min%i==0 and Max%i==0:
        print("%d"%(i), end = " ")



