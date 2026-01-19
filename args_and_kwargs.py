def my_function(*address):
  print("I am from " + address[0])

my_function("Jamalpur", "Dhaka", "Fulzur")

#

def my_function(x, *names):
  for name in names:
    print(x, name)

my_function("Sheikh", "Meghla", "Nurani", "Rafi")


#

def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))
