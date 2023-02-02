# 定義一個二維陣列
array = [[1, 2], [3, 4], [5, 6]]

# 將二維陣列轉換
array = [[row[1], row[0]] for row in array]

# 印出轉換後的二維陣列
for row in array:
    print(row)
    