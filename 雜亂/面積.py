#數學1-1
import math
angel = eval(input("請輸入角度: "))
angel = angel / 180 
lengh = eval(input("請輸入半徑"))

area = 0.5 * lengh* lengh * angel
perimeter = lengh * angel + 2 * lengh
print("面積為%.2fπ"%(area))
print("周長為%.2fπ"%(perimeter))