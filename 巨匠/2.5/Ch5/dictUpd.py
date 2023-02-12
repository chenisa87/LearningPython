scores={'Ch':100,'En':80, 'Ma':95}
print(scores)

add_dic={'So':90}
scores.update(add_dic)
print(scores)

add_dic={'Ma':'N/A'}
scores.update(add_dic)
print(scores)
