results = {"David":0, "Amy":0, "Sean":0}
candidates = ("David", "Amy", "Sean")
for i in range(5) :
    vote = input('投票給: ')
    if(vote not in candidates):
        print('選票無效')
        continue
    results[vote] = results[vote]+1

print("選舉結果:")
for name in candidates:
    print(name, results[name], "票")
