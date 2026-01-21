import datetime

x = datetime.datetime.now()

print(x)

#

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

#

x = datetime.datetime(2024, 12, 14)

print(x.strftime("%A"))