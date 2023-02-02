numbers = list(int(n) for n in input().split(" "))
if numbers[0] >= 1:
    numbers[0] = 1
if numbers[1] >= 1:
    numbers[1] = 1
a= numbers[0]
b = numbers[1]
ans = numbers[2]

check = 0
# >>> AND <<< #
if a == b == ans:
    print("AND")
    check = 1   
# >>> OR <<< #
if a == ans or b == ans:
    print("OR")
    check = 1
# >>> XOR <<< #        
if ans == 1:
    if a != b:
        print("XOR")
        check = 1   
else:
    if a != b:
        pass
    else:
        print("XOR")
        check = 1   
            
if check == 0:
    print("IMPOSSIBLE")
        


    
