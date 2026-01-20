x = lambda a, b, c, d: a * b + c - d
print(x(5, 6, 2, 7))

#

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#

students = [("Meghla", 33), ("Liza", 11), ("Linus", 23)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
