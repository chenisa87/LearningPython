with open('song.txt') as f:
    song = f.read()             # 讀取檔案中歌詞

dict = {}
print("原始歌詞")
print(song)

songLower = song.lower()        # 歌曲改為小寫

for ch in songLower:            # 去掉標點符號
    if ch in ".,?":
        songLower = songLower.replace(ch,'')

songList = songLower.split()    # 將歌曲字串轉成串列

for wd in songList:             # 將歌曲串列處理成字典     
    if wd in dict:              # 檢查此字是否已在字典內
        dict[wd] += 1           # 累計出現次數
    else:
        dict[wd] = 1            # 第一次出現的字建立此鍵與值
    
print("單字及出現次數")
print(dict)                     # 列印字典
