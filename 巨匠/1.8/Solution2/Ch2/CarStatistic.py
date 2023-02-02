carList = ['Audi', 'Toyota', 'Benz', 'BMW', 'Mazda', 'Ford', 'BMW', 'Benz', 'BMW', 'Mazda']
carSet  = {'Audi', 'Toyota', 'Benz', 'BMW', 'Mazda', 'Ford', 'BMW', 'Benz', 'BMW', 'Mazda'}

print("車輛清單:", carList)
print("第三台車是", carList[3-1])
print("共有%d種品牌:"%len(carSet), carSet)

LuxuryCar  = ("Audi", "Benz", "BMW")
LuxuryDict = {"Audi":0, "Benz":0, "BMW":0}
for car in carList :
    if(car in LuxuryCar):
        LuxuryDict[car] = LuxuryDict[car]+1
print("豪華品牌及數量:", LuxuryDict)
