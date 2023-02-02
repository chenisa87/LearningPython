def c2f(c):
    f = 9/5*c+32
    return f 

while(True):
    inStr =input('輸入攝氏溫度(輸入q離開):')
    if(inStr=='q'):
        print('程式結束')
        break
    tc = float(inStr)
    print('攝氏%3d度等於華氏%6.2f度' %(tc,c2f(tc)))
