a = int(input())
b = int(input())
count = total_sum = 0
time = 10
for i in range(a,b+1):
    if i % 4 ==0 or i % 9 == 0:
        print("%-4d"%i,end="")
        count += 1
        total_sum += i
        if count % 10 == 0:
            print()
if count % 10 != 0:
    print()
print(count)
print(total_sum)