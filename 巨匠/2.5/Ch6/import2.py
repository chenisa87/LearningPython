import calculator as temp

tc = float(input("請輸入攝氏溫度:"))
tf = temp.toFahrenheit(tc)

print("攝氏%.2f度等於華氏%.2f度" %(tc,tf))
