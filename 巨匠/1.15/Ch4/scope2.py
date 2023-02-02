a=5
def func( ):
   a=10
   a+=1
   print("func(): a =",a)

print("全域: a =", a)
func( )
a+=1
print("全域: a =", a)
