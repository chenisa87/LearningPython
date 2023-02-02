import random
count_p_win = 0
count_b_win = 0
count_p_b = 0
count_p_c = 0
count_b_c = 0
PEOPLE_END = int(input("玩家到多少停牌:"))
BOT_END = int(input("莊家到多少停牌:"))
CARD = int(input("你要幾副牌:"))
TIMES = int(input("你要執行幾次:"))
for i in range(TIMES): #執行次數
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
    p_c_t = 0
    p_c_c = 0
    b_c_t = 0
    b_c_c = 0
    p_b_t = 0
    #>>>製作遊戲<<<#
    while len(numbers) >= 20: #剩多少副牌停止
        #>>>計算次數<<<#
        people_n = 0
        bot_n = 0
        people_count = 0
        bot_count = 0
        #>>>初始手牌<<<#
        for i in range(2):
            rand_num = random.choice(numbers)
            numbers.remove(rand_num)
            people_n += rand_num
            rand_num = random.choice(numbers)
            numbers.remove(rand_num)
            bot_n += rand_num
        #>>>遊戲開始<<<#
        while True:

            if people_n >= PEOPLE_END:
                pass
            else:
                rand_num = random.choice(numbers)
                numbers.remove(rand_num)
                #print("玩家抽牌:%d"%rand_num)
                people_n += rand_num
                people_count+=1
            if bot_n >= BOT_END:
                pass
            else:
                rand_num = random.choice(numbers)
                numbers.remove(rand_num)
                #print("莊家抽牌:%d"%rand_num)
                bot_n += rand_num
                bot_count+=1
            
            if people_n > 21:
                #print("玩家輸了")
                #print("玩家得點%d"%people_n)
                #print("莊家得點%d"%bot_n)
                b_c_t += 1
                count_b_win+=1
                break
            if bot_n > 21:
                #print("莊家輸了")
                #print("玩家得點%d"%people_n)
                #print("莊家得點%d"%bot_n)
                p_c_t += 1
                count_p_win+=1
                break
            if people_count >= 5:
                #print("莊家輸了")
                #print("玩家得點%d"%people_n)
                #print("莊家得點%d"%bot_n)
                p_c_c += 1
                count_p_c +=1
                break
            if bot_count >= 5:
                #print("玩家輸了")
                #print("玩家得點%d"%people_n)
                #print("莊家得點%d"%bot_n)
                b_c_c += 1
                count_b_c +=1
                break

            if people_n >= PEOPLE_END and bot_n >= BOT_END:
                if people_n > bot_n:
                    #print("莊家輸了")
                    #print("玩家得點%d"%people_n)
                    #print("莊家得點%d"%bot_n)
                    p_c_t += 1
                    count_p_win+=1
                    break
                elif people_n < bot_n:
                    #print("玩家輸了")
                    #print("玩家得點%d"%people_n)
                    #print("莊家得點%d"%bot_n)
                    b_c_t += 1
                    count_b_win+=1
                    break
                else:
                    #print("平手")
                    #print("玩家得點%d"%people_n)
                    #print("莊家得點%d"%bot_n)
                    p_b_t += 1
                    count_p_b+=1
                    break
    print("玩家贏:%d    莊家贏:%d   平手:%d    玩家五龍:%d    莊家五龍:%d"%(p_c_t,b_c_t,p_b_t,p_c_c,b_c_c))
print("玩家贏:%d    莊家贏:%d   平手:%d    玩家五龍:%d    莊家五龍:%d"%(count_p_win,count_b_win,count_p_b,count_p_c,count_b_c))
print("勝率%.2f"%((count_p_win+count_p_c)/(count_p_win+count_b_win+count_b_c+count_p_c)*100))