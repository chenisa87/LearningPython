def f(x, y, z):
   print(x, y, z)
   
li = [1, 2, 3]
f(*li)

f(*range(4, 7))

d = {'x':7, 'y':8, 'z':9}
f(**d)

