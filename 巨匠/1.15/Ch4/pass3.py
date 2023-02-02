def func(thelist):
   print("func()：", id(thelist), thelist)
   thelist = [1,2,3,4]
   print("func()：", id(thelist), thelist)
   return

mylist = [10,20,30]
print("全域：", id(mylist), mylist)
func(mylist)
print("全域：", id(mylist), mylist)
