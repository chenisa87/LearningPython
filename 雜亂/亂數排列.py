import random
count = 1
for i in range(1,15):
    randNum = random.randint(1,100)
    if count % 10 != 0:
        print("%5d"%(randNum),end = "")
    else:
        print("%5d"%randNum)
    count += 1
