# Key Points : Constructors in Python 

# A constructor is a special method in a class used to create and initialize an object of a class. There are different
# types of constructors. Constructor is invoked automatically when an object of a class is created.

# A constructor is a unique function that gets called automatically when an object is created of a class. The main
# purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any
# value other than None.

# Syntax of Python Constructor

# def _init_(self):
# # initializations

# init is one of the reserved functions in Python. In Object Oriented Programming, it is known as a constructor. We
# can also create constructor by defining the function name with same class name.

# ----------------------------------------------------------------------

# class Person:
#     name = "Deepak"
#     occ = "Developer"
#     def info(self):
#         print(f"{self.name} is a {self.occ}")
# a = Person()
# print(a.name) # gives Deepak
# a.name = "Vrinda"
# a.occ = "CEO"
# a.info() 

# on the place of pass vrinda and ceo every time for everyone, we use constructor : 

class Person:
    def __init__(self, n, o): # every time we create a object it's called automatically 
        print("Hey I'm a Person")
        self.name = n 
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Deepak", "CEO")
b= Person("Vrinda", "HR")
c=Person() # error 2 required arguments
# print(a.name) # gives Deepak
# a.name = "Vrinda"
# a.occ = "CEO"
a.info() 
b.info()

# ----------------------------------------------------------------------

# Types of Constructors in Python

# 1. Parameterized Constructor
# 2. Default Constructor

# Parameterized Constructor in Python

# When the constructor accepts arguments along with self, it is known as
# parameterized constructor.

# These arguments can be used inside the class to assign the values to the data
# members.

# Example:

# class Details:
# def __ init_(self, animal, group):
# self.animal = animal
# self.group = group

# obj1 = Details("Crab", "Crustaceans")
# print(obj1.animal, "belongs to the", obj1.group, "group.")

# Output:

# Crab belongs to the Crustaceans group.

# Default Constructor in Python

# When the constructor doesn't accept any arguments from the object and has
# only one argument, self, in the constructor, it is known as a Default
# constructor.

# Example:

# class Details:
# def __ init __ (self):
# print("animal Crab belongs to Crustaceans group")
# obj1=Details()

# Output:

# animal Crab belongs to Crustaceans group

# ----------------------------------------------------------------------
