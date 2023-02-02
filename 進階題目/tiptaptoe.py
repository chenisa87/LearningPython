import random

MAP = 3
map_list = [[0 for i in range(MAP)] for i in range(MAP)]

def checkwin(list):
    check_list = list
    for i in range(MAP): #行判斷
        count_P = 0
        count_B = 0
        for j in range(MAP):
            if check_list[i][j] == "O":
                count_P+=1
            elif check_list[i][j] == "X":   
                count_B+=1
        if count_P == 3: return "win"
        elif count_B ==3: return "loss"
    for i in range(MAP): #列判斷
        count_P = 0
        count_B = 0
        for j in range(MAP):
            if check_list[j][i] == "O":    
                count_P+=1
            elif check_list[j][i] == "X":   
                count_B+=1
        if count_P == 3: return "win"
        elif count_B ==3: return "loss"
    count_P = 0
    count_B = 0
    for i in range(MAP):
        if check_list[i][i] == "O":    
            count_P+=1
        elif check_list[i][i] == "X":    
            count_B+=1
        if count_P == 3: return "win"
        elif count_B ==3: return "loss"
    count_P = 0
    count_B = 0
    for i in range(MAP):
        if check_list[i][MAP-i-1] == "O":    
            count_P+=1
        elif check_list[i][MAP-i-1] == "X":    
            count_B+=1  
        if count_P == 3: return "win"
        elif count_B ==3: return "loss"
    return "pass"

def makeamap(map,n):
    match n:
        case 1:map[0][0] = "O"
        case 2:map[0][1] = "O"
        case 3:map[0][2] = "O"
        case 4:map[1][0] = "O"
        case 5:map[1][1] = "O"
        case 6:map[1][2] = "O"
        case 7:map[2][0] = "O"
        case 8:map[2][1] = "O"
        case 9:map[2][2] = "O"
    return map

def B_map(map):
    n = random.randint(1,9)
    match n:
        case 1:
            if map[0][0] == 0:
                map[0][0] = "X"
            else:B_map(map)
        case 2:
            if map[0][1] == 0:
                map[0][1] = "X"
            else:B_map(map)
        case 3:
            if map[0][2] == 0:
                map[0][2] = "X"
            else:B_map(map)
        case 4:
            if map[1][0] == 0:
                map[1][0] = "X"
            else:B_map(map)
        case 5:
            if map[1][1] == 0:
                map[1][1] = "X"
            else:B_map(map)
        case 6:
            if map[1][2] == 0:
                map[1][2] = "X"
            else:B_map(map)
        case 7:
            if map[2][0] == 0:
                map[2][0] = "X"
            else:B_map(map)
        case 8:
            if map[2][1] == 0:
                map[2][1] = "X"
            else:B_map(map)
        case 9:
            if map[2][2] == 0:
                map[2][2] = "X"
            else:B_map(map)
    return map
def map_map(map):
    print("=========")
    for i in map:
        for j in i:
            print(j,end=" ")
        print()
    print("=========")
while True:
    p_n = int(input())
    map_list =  makeamap(map_list,p_n)
    map_map(map_list)
    check = checkwin(map_list)
    if check == "win":
        print(check)
        break
    elif check == "loss":
        print(check)
        break
    else:
        pass
    map_list = B_map(map_list)
    map_map(map_list)
    check = checkwin(map_list)
    if check == "win":
        print(check)
        break
    elif check == "loss":
        print(check)
        break
    else:
        pass