n = int(input())
num = n // 2
num2 = n % 2

for i in range(num):
    print("1",end="")
if num2 == 0:
    print("0")
else:
    print("1")