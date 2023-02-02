num = eval(input())

for i in range(1,num+1):
    a = i
    for i in range(1,i+1):
        print("%5d"%(a*i), end= " ")
    print()