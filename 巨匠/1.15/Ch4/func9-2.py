def personInfo(name, age, **other):
    print('====info====')
    print("name :", name)
    print("age :", age)
    for key in other:
        print(key, ":", other[key])

personInfo("Sean", 40)
personInfo('David', 35, phone='0987654321', company='IBM')
personInfo('Amy', 28, email='amy@gmail.com', company='Google', gender='Female')


