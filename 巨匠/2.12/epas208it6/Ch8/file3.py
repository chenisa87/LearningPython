poem = '''床前明月光
疑是地上霜
舉頭望明月
低頭思故鄉
'''
try:
    file=open('output2.txt', 'x')
    file.write(poem)
    file.flush()
    file.close()    
    print('資料寫出至output2.txt')
except Exception as e:
    print('資料寫出失敗:', e)
