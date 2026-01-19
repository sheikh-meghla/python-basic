class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Bike(Vehicle):
    def wheelie(self):
        print("Bike is doing a wheelie")

b = Bike()
b.move()
b.wheelie()
