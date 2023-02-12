cars = ['honda','BMW','Toyota','audi']

print("排序之前:", cars)
cars.sort()
print("排序之後:", cars)
cars.sort(reverse=True)
print("反向排序:", cars)
cars.sort(key=len)
print("長度排序:", cars)
cars.sort(key=str.upper)
print("小寫排序:", cars)

