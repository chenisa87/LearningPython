n = []

str_ = input()
characters = "1 2 3 4 5 6 7 8 9 10 11 12"

for x in range(len(characters)):
    str_ = str_.replace(characters[x],"")



str2 = str_.split(".")
del str2[0]
print(str2)