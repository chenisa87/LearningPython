def sumFunc(*other):
    s = 0
    for i in other:
        s+=i
    return s

print(sumFunc(1,2))
print(sumFunc(1,2,3,4,5))
print(sumFunc(1,2,3,4,5,6,7,8,9,10))



