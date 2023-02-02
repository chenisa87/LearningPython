#a = int(input())
#
#while a != 0:
#    print(a % 10 , end="")
#    a //= 10

n = eval(input())

for i in range(1,n+1):
    for a in range(1,n+1):
        print("%-2d*%-2d= %-4d"%(i,a,i*a),end = "")
    print()
