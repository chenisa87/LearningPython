def getResult(s):
    if 60<=score<=100:
        return '及格'
    elif(0<=score<60):
        return '不及格'
    else:        
        raise OverflowError("成績數值錯誤")

score=int(input('輸入成績:'))
try:
    res = getResult(score) 
except OverflowError as e:
    print(e)
else:
    print("考試結果:", res)
