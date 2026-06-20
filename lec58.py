# Key Points : Inheritance in Python 

# Inheritance in python

# When a class derives from another class. The child class will inherit all the public and
# protected properties and methods from the parent class. In addition, it can have its own
# properties and methods,this is called as inheritance.

# Python Inheritance Syntax

# class BaseClass:
# Body of base class
# class DerivedClass(BaseClass) :
# Body of derived class

# Derived class inherits features from the base class where new features can be added to it.
# This results in re-usability of code.

# Types of inheritance:

# 1. Single inheritance
# 2. Multiple inheritance
# 3. Multilevel inheritance
# 4. Hierarchical Inleritance
# 5. Hybrid Inheritance

# ---------------------------------------------------------------------------

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")


e = Employee("Rohan Das", 101)
e.showDetails()
e2 = Programmer("Deepak", 102) # there inheritance is used
e2.showDetails() 
# e2.showLanguage() # not workable as showLanguage is not inherited in Employee, but Employee is inherited in Programmer
e2.showLanguage() # executable coz change Employee into Programmer in e2
# Change class's name from Employee to Programmer, in this condition we use inheritance : 

