import random
n1 = random.randint(1,100)
n2 = random.randint(1,100)
while True:
    rand = random.randint(1,2)
    if rand ==1:
        solution = n1 + n2
        print("%d + %d = "%(n1,n2))
        ans = int(input())
    else:
        solution = n1 - n2
        print("%d - %d = "%(n1,n2))
        ans = int(input())
    if ans == solution:
        break
    else:
        print("try again ")
print("wow u r so good")