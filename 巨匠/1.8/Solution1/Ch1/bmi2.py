height = float(input('請輸入身高，單位為公分: '))
weight = int(input('請輸入體重，單位為公斤: '))
bmi = weight/((height/100)**2)
print("bmi為%9.2fABC" %(bmi))
