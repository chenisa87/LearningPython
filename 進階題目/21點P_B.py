import random
BOT_END = 17 #莊家到多少停牌
CARD = 1
for i in range(1): 
    #>>>創建list<<<#
    number = []
    for j in range(CARD): #你要幾副牌
        for i in range(4):
            for j in range(1,14):
                number.append(j)
    #>>>二次打亂<<<#
    numbers = []
    for i in range(len(number)):
        rand_num = random.choice(number)
        number.remove(rand_num)
        numbers.append(rand_num)
    #>>>製作遊戲<<<#

    #>>>計算次數<<<#
    people_n = 0
    bot_n = 0
    people_count = 0
    bot_count = 0
    giveacard = ""
    #>>>初始手牌<<<#
    rand_num = random.choice(numbers)
    numbers.remove(rand_num)
    people_n += rand_num
    rand_num = random.choice(numbers)
    numbers.remove(rand_num)
    bot_n += rand_num
    rand_num = random.choice(numbers)
    numbers.remove(rand_num)
    people_n += rand_num
    rand_num = random.choice(numbers)
    numbers.remove(rand_num)
    bot_n += rand_num
    print("機器人第一張牌為%d"%rand_num)
    #>>>遊戲開始<<<#
    while True:
        print("玩家手牌%d"%people_n)
        while giveacard != "y" and giveacard != "n":
            giveacard = input("請問你要牌嗎 y/n")
        if giveacard=="y":
            rand_num = random.choice(numbers)
            numbers.remove(rand_num)
            print("玩家抽牌:%d"%rand_num)
            people_n += rand_num
            people_count+=1
            giveacard = ""
        if bot_n >= BOT_END:
            pass
        else:
            rand_num = random.choice(numbers)
            numbers.remove(rand_num)
            print("莊家抽牌")
            bot_n += rand_num
            bot_count+=1
        
        if people_n > 21 or bot_count >= 5:
            print("玩家輸了")
            print("玩家得點%d"%people_n)
            print("莊家得點%d"%bot_n)
            break
        if bot_n > 21 or people_count >= 5:
            print("莊家輸了")
            print("玩家得點%d"%people_n)
            print("莊家得點%d"%bot_n)
            break
        if giveacard == "n" and bot_n >= BOT_END:
            if people_n > bot_n:
                print("莊家輸了")
                print("玩家得點%d"%people_n)
                print("莊家得點%d"%bot_n)
                break
            elif people_n < bot_n:
                print("玩家輸了")
                print("玩家得點%d"%people_n)
                print("莊家得點%d"%bot_n)
                break
            else:
                print("平手")
                print("玩家得點%d"%people_n)
                print("莊家得點%d"%bot_n)
                break