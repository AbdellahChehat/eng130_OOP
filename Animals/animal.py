
#create calss called animal - file name starts with a - class name starts with A
# add common attributes/ var behaviour/ functions
# Syntax class name: class Aniaml:

class Animal : # Defined the class name
    # initialise the class with a builtin method called __init__(self)
    # self refers to current class
    def __int__(self): # Attributes added here
        self.alive = True
        self.spine = True
        self.eyes = True
# Let's create some methods
    def breath(self):
        return "Keep breathing to stay alive"

    def eat(self):
        return "Time to eat!!"


# Create an object of this class

cat = Animal()
# print(cat.breath()) #Calling a method using object of the Animal class
# print(cat.eat())