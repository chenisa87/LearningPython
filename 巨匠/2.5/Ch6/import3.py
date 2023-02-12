from calculator import calcBmi, getMessage

h = int(input('身高:'))
w = int(input('體重:'))
bmi = calcBmi(h,w)
message = getMessage(bmi)

print('BMI值為%.2f, 診斷結果%s' %(bmi,message))
