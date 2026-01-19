class Info:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def Info_x(self):
        return f"{self.name} {self.age}, {self.address}"
# object
info1 = Info("Meghla", 17, "jamalpur")
info2 = Info("Rafi", 26, "jamalpur")

print(info1.Info_x()) 
print(info2.Info_x())