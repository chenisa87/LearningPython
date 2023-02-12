scores={'Ch':100,'En':80, 'Ma':95, 'Na': 90}
print("查詢前成績:", scores)

del scores['Ch']
print("刪除Ch成績:", scores)

scores.clear()
print("清空成績:", scores)

del scores
print("刪除變數:", scores)
