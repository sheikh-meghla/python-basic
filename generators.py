def x():
    yield 5
    yield 30
    yield 1
   
   
for value in x():
    print(value)

