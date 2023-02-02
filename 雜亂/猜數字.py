import random
a = 1
b = 100
LIMIT = int(input("請輸入你想猜的次數:  "))
if LIMIT >=5:
    print("你很破ㄟ 需要%d次"%(LIMIT))

rand_number = random.randint(a,b)
print("請輸入數字%d ~ %d:  "%(a,b))
while LIMIT > 0:
    while True:
        guess_num = int(input())
        if a < guess_num < b:
            break
        else:
            print("請輸入數字%d ~ %d哦:  "%(a,b))
    if guess_num == rand_number:
        print("You win this game!!!")
        break    
    else:
        LIMIT -= 1
        if LIMIT == 0:
            print("笑死你這個小廢物答案是%d"%rand_number)
            break
        if rand_number >= guess_num:
            a = guess_num
        else:
            b = guess_num
        print("你猜錯摟你還有%d次機會"%LIMIT)
        print("請輸入數字%d ~ %d:  "%(a,b))
