# >>> 初始輸入 <<< #
n = int(input())
checkturn = int(input())
if checkturn == 0:
    x = ["a","b","c","d"]
elif checkturn == 1:
    x = ["b","c","d","a"]
elif checkturn == 2:
    x = ["c","d","a","b"]
elif checkturn == 3:
    x = ["d","a","b","c"]
firstans = []
for i in range(n):
    firstans.append(list(map(int, input().rstrip().split())))
def makealist():
    ans = []
    for i in range(1,n+1):
        for j in range(i):
            if i % 2 == 1:  ans.append(x[0])
            else:    ans.append(x[2])
        for j in range(i):
            if i % 2 == 1:  ans.append(x[1])
            else:    ans.append(x[3])
    ans.reverse()
    for i in range(n+1):
        del ans[0]
    ans.reverse()
    return(ans)
def makeans():
    ans = makealist()
    i = (n-1) // 2
    j = (n-1) // 2
    endans = []
    endans.append(firstans[i][j])
    for a in range(n*n-1):
        check = ans[a]
        if check == "a":
            j -= 1
        elif check == "b":
            i -= 1
        elif check == "c":
            j += 1
        elif check == "d":
            i += 1
        endans.append(firstans[i][j])
    return endans
ans_list = makeans()
for i in ans_list:
    print(i,end="")