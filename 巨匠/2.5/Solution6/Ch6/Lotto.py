import random

lottoNums = random.sample(range(1, 50), 6)

specialNum = random.randint(1,49)
while(specialNum in lottoNums):
    specialNum = random.randint(1,49)

print('樂透號碼:', sorted(lottoNums))
print('特別號:', specialNum)
