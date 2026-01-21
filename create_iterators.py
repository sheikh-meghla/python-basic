class Num:
  def __iter__(self):
    self.a = 2
    return self

  def __next__(self):
    x = self.a
    self.a += 4
    return x

myclass = Num()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))