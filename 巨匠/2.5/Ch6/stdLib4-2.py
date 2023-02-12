from datetime import date

now = date.today() # 現在時間
print(now, "星期:", now.isoweekday())

#設定顯示格式      06-09-21. 09 Jun 2021.
print(now.strftime('%m-%d-%y. %d %b %Y.'))

birthday = date(1974, 3, 21) # 指定日期date物件

age = now - birthday
print(age.days) # 以天計算年紀
