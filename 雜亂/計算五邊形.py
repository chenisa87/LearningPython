import math
#s = eval(input("邊長"))

#area = 5 * math.pow(s,2) / (4*math.tan(math.pi/5))

#print("面積為%.2f"%(area))

n = eval(input("請輸入有幾個邊"))
s = eval(input("請輸入邊長為多少"))


area = n * math.pow(s,2) / (4*math.tan(math.pi/n))

print(format(area,'10.2f'))