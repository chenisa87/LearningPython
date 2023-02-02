min = eval(input("請輸入幾分鐘"))
sec = eval(input("請輸入幾秒鐘"))
km = eval(input("請輸入幾公里"))

speed = km / (min + sec / 60) / 60
print("你的速度是%.2f公里每一小時"%(speed))