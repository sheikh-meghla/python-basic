def x(func):
  def myinner():
    return func().upper()
  return myinner

@x
def myfunction():
  return "Hello"

print(myfunction())

#


def x(func):
  def y(x):
    return func(x).upper()
  return y

@x
def myfunction(nam):
  return "Hello " + nam

print(myfunction("meghla"))

