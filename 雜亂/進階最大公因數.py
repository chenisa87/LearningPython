numbers = input()
num_list = numbers.split()
str_list = ",".join(num_list)
num_list = list(map(int, num_list))
count = 0
num_ends = 0
i = 1
continue_ = True


while continue_:
    count = 0
    for num in num_list:
        if i > num:
            continue_ = False
    for num in num_list:
        if num % i == 0:
            count += 1
            continue
        else:
            break
    if count == len(num_list) and i >= num_ends:
        num_ends = i 

    i += 1 
print("gcd(%s) = %d"%(str_list,num_ends))
