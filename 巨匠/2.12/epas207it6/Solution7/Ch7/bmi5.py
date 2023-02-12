def calcBMI(h,w):
    return w/((h/100)**2)

def diagnose(bmi):
    if(bmi>30):
        result = '肥胖'
    elif(bmi>25):
        result = '過重'
    elif(bmi>18.5):
        result = '正常'
    elif(bmi>0):
        result = '過輕'
    else:
        raise OverflowError('BMI數值錯誤'+str(bmi))
    return result

try :
    height = float(input('請輸入身高，單位為公分: '))
    weight = int(input('請輸入體重，單位為公斤: '))
    if height<0:
        raise ZeroDivisionError('身高數值錯誤:'+str(height))
    bmi = calcBMI(height, weight)
    print("bmi: %.2f, 判定結果: %s" %(bmi, diagnose(bmi)))
except ValueError as e:
    print('身高體重請輸入數值,', e)
except ZeroDivisionError as e:
    print('身高請輸入正值,', e)
except OverflowError as e:
    print('體重請輸入正值,', e)
