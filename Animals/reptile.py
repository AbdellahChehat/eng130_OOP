from animal import Animal # file name then Class name

# Create a class called reptile

class Reptile (Animal) : #inherit from Animal Class

    def __int__(self):
        super().__int__() # super is used to inherit everything from the parent class
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chambers = [3, 4]

    def hunt(self):
        return "keep working hard to find food"

    def use_venom(self):
        return "If I have I will use"


smart_reptile = Reptile()
print(smart_reptile.breath())
print(smart_reptile.hunt())