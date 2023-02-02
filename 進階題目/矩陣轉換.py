# >>> 輸入 <<< #
arr = input()
arr = [int(n) for n in arr.split()]
row = arr[0]
colun = arr[1]
test = arr[2]
list_num = []
for i in range(row):
    list_num.append(list(map(int, input().rstrip().split())))
check = input()
check = [int(n) for n in check.split()]



def a(list):
    list_num = list
    list_after = [[0 for _ in range(len(list_num))]  for _ in range(len(list_num[0]))]
    for i in range(len(list_num)):
        for j in range(len(list_num[0])):
            list_after[j][len(list_num)-i-1] = list_num[i][j]
    list_num = list_after
    return list_num

def b(list):
    list_num = list
    list_after = [[0 for _ in range(len(list_num[0]))]  for _ in range(len(list_num))]
    for i in range(len(list_num)):
        for j in range(len(list_num[0])):
            list_after[len(list_num)-i-1][j] = list_num[i][j]
    list_num = list_after
    return list_num

for i in check:
    if i == 0:
        list_num = a(list_num)
    else:
        list_num = b(list_num)
# >>> 輸出 <<< #
print(">>>>> 輸出 <<<<<")
print("%d %d"%(len(list_num),len(list_num[0])))
for i in range(len(list_num)):
    for j in range(len(list_num[0])):
        print("%d"%list_num[i][j],end=" ")
    print("")