inStr = input('輸入字串:')
reStr = inStr[::-1]

if(inStr==reStr):
    print(inStr, "是迴文")
else:
    print(inStr, "不是迴文")
