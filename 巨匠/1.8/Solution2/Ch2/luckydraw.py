prizes = ['汽車一輛','獎金十萬','家庭劇院一組',
          '筆記型電腦一台','iPhone 手機一支',
          'Switch遊樂器一台',
          '飯店住宿券一張','飯店住宿券一張',
          '下午茶券兩張','下午茶券兩張']

no = int(input('輸入摸彩號碼:'))-1

if(no<len(prizes)):
    print('恭喜抽中', prizes[no])
else:
    print("銘謝惠顧，明年還有機會")
