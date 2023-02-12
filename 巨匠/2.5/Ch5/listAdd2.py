list1= ['a', 'b', 'c']
print("擴展之前:", list1)
print("擴展之前長度 = ", len(list1))

list1.extend(["def","ghij"])
print("擴展之後:", list1)
print("擴展之後長度 = ", len(list1))
print("擴展元素: ", list1[3], list1[4])
