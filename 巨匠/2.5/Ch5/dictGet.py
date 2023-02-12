scores={'Ch':100,'En':80, 'Ma':95, 'Na': 90}
print("查詢前成績:", scores)

ch_score = scores.get('Ch')
print('國語考%s分' %ch_score)
en_score = scores.get('En', 'N/A')
print('英文考%s分' %en_score)
ma_score = scores.pop('Ma', 'N/A')
print('數學考%s分' %ma_score)
so_score = scores.pop('so', 'N/A')
print('社會考%s分' %so_score)

print("查詢後成績:", scores)
