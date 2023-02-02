import math
month = int(input("請輸入你要放幾個月"))
money = int(input("請輸入你要存入的薪水"))
rate = eval(input("請輸入一個月幾%"))

currentValue = money*math.pow(1+rate/100,month)

print("把%s放入銀行%s個月能獲得%d"%(money,month,currentValue))







