total = eval(input("請輸入你要執行幾次  "))
for i in range(total):
    num = int(input("糗輸入你要加的數字 "))
    ans = 0
    while num != 0:
        ans += num % 10
        num = num // 10
    print(ans)
