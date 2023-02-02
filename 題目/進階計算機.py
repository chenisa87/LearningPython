num_list = []
num = str(input())
a = 0
for num in num:
    num_list.append(num)
if "+" in num_list:
    a = 1
elif "-" in num_list:
    a = 2
elif "*" in num_list:
    a = 3
elif "/" in num_list:
    a = 4
elif "%" in num_list:
    a = 5
else:
    print("三小拉")
sum = num.split('+')
print(num_list)
print(a)
print(sum)
