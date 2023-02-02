num1 , num2 , num3 = eval(input("num,num,num"))
if num1 < num2:
    num1,num2 = num2,num1 # 1 > 2
if num2 < num3:
    num2,num3 = num3,num2 # 2 < 3
if num1 < num2:
    num1,num2 = num2,num1 # 1 > 2
print(num1,num2,num3)
