coin1 = 20
coin5 = 10
coin10 = 3
coin50 = 2
coin_total = coin50*5+coin10*10+coin5*5+coin1*1
print('硬幣總值:', coin_total)

bill100 = 3
bill200 = 2
bill500 = 1
bill1000 = 2
bill_total = (bill100+bill200*2+bill500*5+bill1000*10)*100
print('紙鈔總值:', bill_total)

print("總金額:", bill_total+coin_total, "元")
