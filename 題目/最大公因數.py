n1,n2=map(int,input().split()) #將輸入值的空白隔開，並各自轉成int
list1=[n1,n2]
i = min(list1)
while True:
    try:
        if n1 % i == 0 and n2 % i == 0:
            print("最大公因數為:%d"%i)
            break
        else:
            i = i - 1           
    except:
        break