count = 0
for a in range(1,1001):
    for b in range(1,1001):
        for c in range(1,1001):
            if a*a*a + b*b*b == c*c*c:
                count+=1
                if count==1:
                    print("%.3d平方 + %.3d平方 = %.3d三方"%(a,b,c))
                    break
            print(a,b,c)