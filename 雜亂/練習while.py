import random
again = 1
while again ==1:
    randNum = random.randint(1,101)
    print(randNum)
    while True:
        again = eval(input("continue:1 or quit:0----->"))
        if again ==1 or again ==0:
            break
        else:
            print("please input 1 or 0")

print("ok bye")