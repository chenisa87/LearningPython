import random

def bot_check(num, win, Range):
    if (win - num)%Range == 0:
        return Range
    else:
        return (win - num)%Range

def Game():
    total = 0
    win = random.randint(21,100)
    Range = random.randint(3,10)
    bot = bot_check(total, win, Range)
    player = int(input("請先決定誰開始\n0 -> 先 \n1 -> 後\n輸入:"))
    print(f"請搶到{win}吧!!\n--Game Start--")
    for i in range(100):
        if total > win:
            print("數字超過ㄌ!!")
            break

        if player == 1:
            print(f"機器人輸入{bot}")
            total = total + bot
            print(f"目前總數{total}")

            if total == win:
                print("你輸ㄌQQ")
                break
                    
            n = int(input(f"請輸入數字1~{Range}:"))
            print(f"你輸入{n}")
            total = total + n
            print(f"目前總數{total}")

            if total == win:
                print("你贏ㄌ!!!")
                break
        else:
            n = int(input(f"請輸入數字1~{Range}:"))
            print(f"你輸入{n}")
            total = total + n
            print(f"目前總數{total}")

            if total == win :
                print("你贏ㄌ!!!")
                break

            print(f"機器人輸入{bot}")
            total = total + bot
            print(f"目前總數{total}")

            if total == win:
                print("你輸ㄌQQ")
                break

while True:
    Game()
    angin = input("你還要再玩嗎?\n是:Y or 否:N\n輸入:")
    if angin == "Y":
        Game()
    else:
        print("掰掰~~")
        break