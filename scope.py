x = "Hi Liza"
def myfunc():
  y = "Hello Meghla"
  print(y)

myfunc()
print(x)

#

def myfunc():
  global x
  x = 6
myfunc()

print(x)