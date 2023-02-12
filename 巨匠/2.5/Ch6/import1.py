import calculator

r = int(input('請輸入圓半徑(公分):'))
area = calculator.calcArea(r)

print('半徑為%d公分的圓,面積為%.2f平方公分' %(r,area))
