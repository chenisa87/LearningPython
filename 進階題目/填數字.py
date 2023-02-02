n  = int(input())
list = [[0 for _ in range(n)] for _ in range(n)]

i = (n-1)//2
j = 0

for x in range(1,n*n+1):
    list[i][j] = x
    i_f = i
    j_f = j
    i -= 1
    j -= 1

    if i < 0:
        i = n-1
    if j < 0:
        j = n-1
    if list[i][j] == 0:
        pass
    else:
        i = i_f
        j = j_f
        i += 1
        if i > n-1:
            i = 0
for x in list:
    for y in x:
        print("%.2d"%y,end=" ")
    print()    
    