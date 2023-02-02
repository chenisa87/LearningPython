from random import randint
def map(list):
    map_list = list
    print("---------")
    print("-%s--%s--%s-"%(map_list[0],map_list[1],map_list[2]))
    print("---------")
    print("-%s--%s--%s-"%(map_list[3],map_list[4],map_list[5]))
    print("---------")
    print("-%s--%s--%s-"%(map_list[6],map_list[7],map_list[8]))
    print("---------")

def map_p(list):
    map_p_l = list
    n = int(input("你要在第幾格:"))
    if map_p_l[n-1] == "#":
        map_p_l[n-1] = "O"
    else:
        print("這個已經有了喔")
        map_p(map_p_l)
    return map_p_l


def map_b(list):
    map_b_l = list
    n = randint(1,9)
    if map_b_l[n-1] == "#":
        map_b_l[n-1] = "X"
    else:
        map_b(map_b_l)
    return map_b_l

def checkwin(list):
    map_w = list
    for i in range(3):
        check_p = 0
        check_b = 0
        for j in range(i*3,3*(i+1)):
            check_p += 1 if map_w[j] == "O" else 0 
            check_b += 1 if map_w[j] == "X" else 0
        if check_b == 3:
            return "bot_win"
        elif check_p == 3:
            return "people_win"
        check_p = 0
        check_b = 0
        for j in range(i,9,3):
            check_p += 1 if map_w[j] == "O" else 0 
            check_b += 1 if map_w[j] == "X" else 0
        if check_b == 3:
            return "bot_win"
        elif check_p == 3:
            return "people_win"
    if map_w[0] == "O" and map_w[4] == "O" and map_w[8] == "O":
        return "people_win"
    elif map_w[0] == "X" and map_w[4] == "X" and map_w[8] == "X":
        return "bot_win"
    elif map_w[2] == "O" and map_w[4] == "O" and map_w[6] == "O":
        return "people_win"
    elif map_w[2] == "X" and map_w[4] == "X" and map_w[6] == "X":
        return "bot_win"
    else:
        return "nothing"



def game():
    map_l = ["#","#","#","#","#","#","#","#","#"]  
    map(map_l) 
    while True:
        map_l = map_p(map_l)
        map(map_l)
        if checkwin(map_l) == "people_win":
            print("恭喜你獲勝!")
            break
        elif checkwin(map_l) == "bot_win":
            print("對方獲勝 T_T ")
            break
        else:
            pass
        map_l = map_b(map_l)
        map(map_l)
        if checkwin(map_l) == "people_win":
            print("恭喜你獲勝!")
            break
        elif checkwin(map_l) == "bot_win":
            print("對方獲勝 T_T ")
            break
        else:
            pass

game()
