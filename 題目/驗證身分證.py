dic = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13 , 'E' : 14,  #先建立字典
       'F' : 15, 'G' : 16, 'H' : 17, 'I' : 34, 'J': 18,
       'K' : 19, 'L' : 20, 'M' : 21, 'N' : 22, 'O' : 35,
       'P' : 23, 'Q' : 24, 'R' : 25, 'S' : 26, 'T' : 27,
       'U' : 28, 'V' : 29, 'W' : 32, 'X' : 30, 'Y' : 31,
       'Z' : 33}
try:
    while(True):
        str = input()
        digits = int(dic[str[0]])%10 #取出字典的值進行運算
        ten_digits = int(dic[str[0]])//10
        sum = digits*9 + ten_digits
        for i in range(1,9):
            sum += int(str[i])*(9-i)
        sum += int(str[9])
        if(sum % 10 == 0):
            print("real")
        else:
            print("fake")
       
except EOFError:
    pass