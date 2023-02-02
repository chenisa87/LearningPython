def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


def test(a,b,c):
    return lambda x : x + a*b*c

testa = test(2,5,3)

testaaa = testa(11)

print(testaaa)