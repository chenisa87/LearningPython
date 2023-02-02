cost = eval(input(""))

if cost >= 38000:
    cost = cost*0.7
elif cost >= 28000:
    cost = cost*0.8
elif cost >= 18000:
    cost = cost*0.9
elif cost >= 8000:
    cost = cost*0.95
print(cost)    