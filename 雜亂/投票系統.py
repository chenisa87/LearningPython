n = int(input("請問有幾張票"))
num1 = 0
num2 = 0
num3 = 0

for i in range(n):
    num = eval(input("請問你想投給誰 1號/2號/廢票:  "))
    if num == 1:
        num1 += 1
    elif num == 2:
        num2 += 1
    else:
        num3 += 1
    print("一號候選人得%d票\n二號候選人得%d票\n廢票%d票"%(num1,num2,num3))
    
if num1 == num2:
    print("平手")
if num1 > num2:
    print("得票數最高得是一號候選人 總共得了%d票"%num1)
else:
    print("得票數最高得是二號候選人 總共得了%d票"%num2)