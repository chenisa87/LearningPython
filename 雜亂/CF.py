print("%s %6s"%("華氏","攝氏"))
for F in range(10,250,10):
    C = 5/9*(F-32)
    print("%-4d %8.2f"%(F,C))