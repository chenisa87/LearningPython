Sean, David, Amy = 0,1,2
Ch, En, Ma = 0, 1, 2

scores = [[70, 80, 90],
          [60, 55, 70],
          [77, 88, 99]]

print("Sean的成績", scores[Sean])
print("David數學分數:", scores[David][Ma])
scores.sort(key=sum)
print("總成績排序:")
for s in scores:
    print(s)
