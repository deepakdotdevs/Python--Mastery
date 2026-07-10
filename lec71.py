# Key Points : Operator Overloading in Python 

# Operator Overloading in
# Python: An Introduction

# Operator Overloading is a feature in Python that allows
# developers to redefine the behavior of mathematical and
# comparison operators for custom data types. This means
# that you can use the standard mathematical operators (+, -,
# *,/, etc.) and comparison operators (>, <, == , etc.) in your
# own classes, just as you would for built-in data types like int,
# float, and str.

# Why do we need operator overloading?

# Operator overloading allows you to create more readable
# and intuitive code. For instance, consider a custom class
# that represents a point in 2D space. You could define a
# method called 'add' to add two points together, but using
# the + operator makes the code more concise and readable:

# -----------------------------------------------------------------------------------

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j 
        self.k = k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self, x): # it is the example of operator overloading here
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)
v1 = Vector(3,5,6)
print(v1)
v2 = Vector(1,2,3)
print(v2)

print(v1+v2) # gives error we have to define it as __add__ method here in this program resultant output i string we have to change into vector
print(type(v1+v2))
