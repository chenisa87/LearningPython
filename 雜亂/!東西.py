n = 10

for i in range(1,n+1):
    num = 1
    for j in range(1,i+1):
        num *= j
    print("#%2d! = %d"%(i,num))
