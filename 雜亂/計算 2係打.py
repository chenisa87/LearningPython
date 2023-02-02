import math

#a = eval(input(""))
#a = a/180 * math.pi
#c = 2*math.sin(a)*math.cos(a)

#print(c)

sin = eval(input("")) / 180 * math.pi
cos = eval(input("")) / 180 * math.pi

sin2 = 2*math.sin(sin)*math.cos(cos)
cos2 = math.pow(math.cos(cos),2) - math.pow(math.sin(sin),2)
print(sin2)
print(cos2)
