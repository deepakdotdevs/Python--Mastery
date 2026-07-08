# Key Points -> dir, __dict__ and help method in python 

# The dir() method

# dir() : The dir0 function returns a list of all the attributes and
# methods (including dunder methods) available for an object. It is a
# useful tool for discovering what you can do with an object.
    
# dict __ attribute returns a dictionary
# representation of an object's attributes. It is a useful tool for
# introspection.

# help() : The helpO function is used to get help documentation for
# an object, including a description of its attributes and methods.

# ---------------------------------------------------------------

# dir() program : 

# x = [1,2,3] # this is a list
# print(dir(x)) # tells every function/method we can do with that object
# print(x.__add__) # tells about the add method

# y = (5,6,7) # tuple
# print(dir(y))
# print(y.__add__)

# ---------------------------------------------------------------

# dict() program & help() program : 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p = Person("Deepak", 21)

print(p.__dict__) # returns dictionary representation of the data

print(help(Person)) # returns documentation of it with every brief