import random

def bnumber(n,l,e):
    number = n
    rnum = l % (e+1) #得到 remainder 2 # 5 13
    times = number // (e+1) + 1 
    bn = rnum + (e+1)*times - number
    if bn > e:
        bn -= e+1
    if bn ==0:
        bn = random.randint(1,e)
    else:
        pass

    
    return bn

def checkwin(add,number,limit,judge):
    n = number
    if judge == 1:
        n = add+n
        if n == limit:
            print(">>>>恭喜你贏了<<<<")
            return 500
        else:
            return n
    else:
        n = add +n
        if n == limit:
            print("機器人輸入%d"%add)
            print("現在到%d"%n)
            print(">>>>笑死你輸了<<<<")
            return 500
        else:
            return n

count = 1
def game(count):
    number = 0
    limit = random.randint(10,100)
    enumber = random.randint(2,9)
    print("這是你第%d次挑戰"%count)
    first = int(input("先/後 輸入 1/2 : "))
    print("先到%d就贏了"%limit)
    print("請輸入數字1到%d"%enumber)
    print(">>>>>>>正賽開始<<<<<<<")
    while True:
        if first ==1:
            pnum = int(input("請輸入數字:"))
            number = checkwin(pnum,number,limit,1)
            if number == 500:
                break
            print("現在到%d"%number)
        else:
            pass
        bnum = bnumber(number,limit,enumber) # 現在的數字 最大的數字 每次幾個數字
        number = checkwin(bnum,number,limit,2)
        if number == 500:
            break
        print("機器人輸入%d"%bnum)
        print("現在到%d"%number)
        first = 1
    count += 1
    again = str(input("請問你還要玩嗎輸入 y/n : "))
    if again == "y":
        game(count)
    else:
        print("全部關閉")



game(count)