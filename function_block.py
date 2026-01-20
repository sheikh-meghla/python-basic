def x():
    print("Hello")
    print("Welcome")

x()
def myfuntion(n):
  return lambda a : a * n

y = myfuntion(2)

print(y(11))