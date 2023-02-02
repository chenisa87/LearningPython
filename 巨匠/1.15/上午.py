arr=[int(i) for i in input().split()]
print("%d"%((arr[0]+arr[1])%7) if (arr[0]+arr[1])%7!=0 else 7)
