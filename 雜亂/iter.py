class MyNumbers:
  def __init__(self,a,b):
    self.a = a
    self.b = b
  def __iter__(self):
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += self.b
      return x
    else:
      raise StopIteration

myclass = MyNumbers(3,5)
myiter = iter(myclass)

for x in myiter:
  print(x)