scores={'Ch':100,'En':80, 'Ma':95}
print("科目排序:", sorted(scores))
print("成績排序:", sorted(scores.values()))

print("科目反向排序:", sorted(scores,reverse = True))
print("成績反向排序:", sorted(scores.values(),reverse = True))
