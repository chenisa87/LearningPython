poem = '''床前明月光
疑是地上霜
舉頭望明月
低頭思故鄉
'''
try:
    with open('output3.txt', 'a') as f:
        f.write(poem)
    print('資料寫出至output3.txt')
except Exception as e:
    print('資料寫出失敗:', e)
