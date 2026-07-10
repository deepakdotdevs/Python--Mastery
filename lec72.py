# Key Points -> Single Inheritance in Python : 

# Single Inheritance in Python

# Single inheritalce is a type of inheritance where a class inherits
# properties and behaviors from a single parent class. This is the simplest
# and most common form of inheritance.

# Syntax

# The syntax for single inheritance in Python is straightforward and easy to
# understand. To create a new class that inherits from a parent class,
# simply specify the parent class in the class definition, inside the
# parentheses, like this:

# class ChildClass(ParentClass) :
# # class body

# --------------------------------------------------------------------------------

# Program 1 : 

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#     def make_sound(self):
#         print("Sound made by the animal")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
#     def make_sound(self):
#         print("Bark!")

# D = Dog("Dog", "Doggerman")
# D.make_sound()

# a = Animal("Dog", "Dog")
# a.make_sound()

# Program 2 : 

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def details(self):
        print(f"i have a {self.name} which is {self.color} in color")
class Cat(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, color="gray")
        self.age = age
    def details(self):
        print(f"i have a {self.name} which is {self.color} in color whoes age is {self.age}")
    
ani = Animal("Tiger", 'black & white')
ani.details()

ani1 = Cat('cat', 7)
ani1.details()