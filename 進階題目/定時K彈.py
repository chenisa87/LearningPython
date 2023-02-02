"""
N個人
數到M就會爆炸
總共爆炸K次
"""

N = int(input("請輸入總人數:"))
M = int(input("請輸入第幾個人會爆炸:")) 
K = int(input("請輸入總共爆炸幾次:"))
N_list = [int(n) for n in range(1,N+1)]

print(N_list)

def boom():
    X = M-1
    while True:
        if X >= len(N_list):
            X -= len(N_list)
        else:
            break
    del N_list[X]
    for i in range(X):
        N_list.append(N_list[0])
        del N_list[0]


for i in range(K): #1 2 3 4 5
    boom()         #1 3 4 5


print(N_list[0])