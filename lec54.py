# Key Points -> Classes and Objects in Python : 

# A class is a blueprint or a template for creating objects, providing initial values
# for state (member variables or attributes), and implementations of behavior
# (member functions or methods). The jiser-defined objects are created using
# the class keyword.

# Creating a Class:

# Let us now create a class using the class keyword.

# class Details:
# name = "Rohan"
# age 20

# Creating an Object:

# Object is the instance of the class used to access the properties of the class
# Now lets create an object of the class.
    
# Example:

# obj1 = Detatls()

# Now we can print values:

# Example:

# class Detatls:
# name = "Rohan"
# age = 20

# obj1 = Detatls()
# print(obji.name)
# print(obji.age)

# Output:

# Rohan

# 20

# self parameter : 
# the self Parameter Is the re Ref To the current instance Of the class 
# And is used to access Variables That belongs to the class It must be provided 
# As the extra parameter Inside the method definition


# -------------------------------------------------------

# make class using class keyword

class Person:
    name = "Deepak"
    occupation = "AI Engineer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

# now i wants to make a new person, we we use class here
a = Person() # Object of the class
b = Person()
c= Person()
a.name = "Shubham"
a.occupation = "Accountant"
b.name = "Rakesh"
b.occupation = "HR"
# print(a.name, a.occupation, a.network)

a.info()
b.info()
c.info() # takes default parameters

# -------------------------------------------------------
