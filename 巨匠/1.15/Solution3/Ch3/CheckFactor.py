num = int(input('輸入整數:'))

if(num%2==0 and num%3==0):
    print('%d是2的倍數,也是3的倍數' %num)
elif(num%2==0):
    print('%d是2的倍數' %num)
elif(num%3==0):
    print('%d是3的倍數' %num)
else:
    print('%d不是2的倍數,也不是3的倍數' %num)

##if(num%2==0):
##    print('%d是2的倍數' %num, end='')
##    if(num%3==0):
##        print(',也是3的倍數')        
##else:
##    if(num%3==0):
##        print('%d是3的倍數' %num)
##    else:
##        print('%d不是2的倍數,也不是3的倍數' %num)



