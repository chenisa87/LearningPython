filename = input('請輸入讀取檔名:')

fin = open(filename)
line = fin.readline()

while line:
    print(line, end='')
    line = fin.readline()
