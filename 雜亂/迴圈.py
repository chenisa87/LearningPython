for i in range(1,10):
    a = i
    for i in range(1,10):
        b = a * i
        print("%d*%d=%2d"%(a,i,b),end = " ")
    print("")