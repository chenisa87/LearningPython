number  = int(input())

while True:
    n = number % 10
    if n > 0:
        print("%d"%n,end="")
    else:
        pass
    number = number // 10
    if number ==0:
        break