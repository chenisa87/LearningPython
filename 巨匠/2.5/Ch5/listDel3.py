cars = ['Honda','Toyota','Ford','BMW','Mazda','Benz']     
print("刪除之前:", cars)
print("刪除之前長度 = ", len(cars))

del cars[4]
print("刪除之後:", cars)
print("刪除之後長度 = ", len(cars))

del cars[1:3]
print("刪除之後:", cars)
print("刪除之後長度 = ", len(cars))  
