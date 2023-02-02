a=5
def func( ):
   global a
   a=a+1
   print("func(): a =",a)

print("全域: a =", a)
func( )
a=a+1
print("全域: a =", a)
