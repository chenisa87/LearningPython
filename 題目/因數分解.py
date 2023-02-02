Number = int(input())
i = 2
First_Num = True #用來防止 100 
print("%d = "%Number,end="")
while(Number >= i):
    count = 0
    while(Number % i ==0):
        Number = Number // i
        count +=1
    if count > 1 and First_Num == True:
        print("%d^%d"%(i,count),end = "")
        First_Num = False
    elif count ==1 and First_Num == True:
        print("%d"%i,end = "")
        First_Num = False
    elif count > 1 and First_Num == False:
        print(" * %d^%d"%(i,count),end = "")
    elif count ==1 and First_Num == False:
        print(" * %d"%i,end = "")
    else:
        i=i+1