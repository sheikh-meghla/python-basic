def my_function(x):
  print(x + " Ahmed")

my_function("Meghla")
my_function("Rafi")
my_function("Nurani")

#

def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Sheikh", "Meghla")

#

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Raifa", "age": 2}
my_function(my_person)

#

def my_function(x, y):
  return x * y - x * x

result = my_function(100, 500)
print(result)

#

def my_function():
  return ["apple", "banana", "cherry",]
fruits = my_function()
print(fruits[0])
