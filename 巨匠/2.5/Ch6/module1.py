import math

print('請輸入直角三角形兩邊長:')
x = float(input('底邊長:'))
y = float(input('高邊長:'))
z = math.sqrt(x**2+y**2)
print('斜邊長:', z)
