row_column = input()
row_column = [int(n) for n in row_column.split(" ")]
arr = []
for i in range(row_column[0]):
    arr.append(list(map(int, input().rstrip().split())))
def add():
    global addnum 
    global add_list 
    add_list = []
    addnum = 0
    for i in range(row_column[0]):
        max_num = 0
        for number in arr[i]:
            if number >= max_num:
                max_num = number
        addnum += max_num
        add_list.append(max_num)
    print(addnum)

def checkS():
    check = False
    for numbers in add_list:
        if addnum % numbers == 0:
            print(numbers,end=" ")
            check = True
    if check == False:
        print(-1)
add()
checkS()