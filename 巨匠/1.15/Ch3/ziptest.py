subjs = ['國語', '數學', '英文']
scores = [100, 80, 95]

for i in range(len(subjs)):
    print('%s分數:%d' %(subjs[i],scores[i]))

print(list(zip(subjs, scores)))

for n, s in list(zip(subjs, scores)):
    print('%s分數:%d分' %(n,s))
