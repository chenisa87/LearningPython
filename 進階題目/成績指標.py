sump = int(input("總人數:"))
arr = input()
arr = [int(n) for n in arr.split(" ")]

fail = []
pass_ = []

for i in range(sump):
    if arr[i] < 60:
        
        fail.append(arr[i])
    else:
        pass_.append(arr[i])

def checkfail():
    if fail == []:
        return "best case"
    else:
        maxnum = max(fail)
        return maxnum

def checkpass():
    if pass_ == []:
        return "worst case"
    else:
        minnum = min(pass_)
        return minnum 
print(">>>output<<<")
# >>>印出第一個東西<<< #
arr = list(map(str,arr))
arr = " ".join(arr)
print(arr)
# >>>第二行<<< #
mfn = checkfail()
print(mfn)
# >>>第三行<<< #
mpn = checkpass()
print(mpn)