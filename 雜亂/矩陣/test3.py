count = 1
A = []
for i in range(0, 3):
    temp = []
    for j in range(0, 4):
        temp.append(count)
        count += 1
    A.append(temp)
print(A)