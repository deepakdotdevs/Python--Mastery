# Key Points : Static Methods in Python 

# We use static methods when we don't need class's instance anymore
# Static methods in Python are methods that belong to a class rather
# than an instance of the class. They are defined using the
# @staticmethod decorator and do not have access to the instance of
# the class (i.e. self). They are called on the class itself, not on an
# instance of the class. Static methods are often used to create utility
# functions that don't need access to instance data.

# class Math:
# @staticmethod
# def add(a, b):
# return a + b

# result = Math.add(1, 2)
# print(result) # Output: 3

# In this example, the add method is a static method of the Math
# class. It takes two parameters a and b and returns their sum. The
# method can be called on the class itself, without the need to create
# an instance of the class.
    
# ----------------------------------------------------------------------------------\

# Program : 

class Math:
    def __init__(self, num):
        self.num = num
    def addtonum(self, n): # add new no. n in num
        self.num = self.num + n
    @staticmethod
    def add(a,b):
        return a+b
a = Math(5)
print(a.num)  # 5
a.addtonum(6)
print(a.num) # 11

# Let's supporse for some reason in the same class i want to add a Utility method
# coz sometime i want to add two nos within the class so there we make static method
# it is not essential that we have to call static method in or with instance
# we can call it directly, it's like a normal method but only be in the class

print(a.add(7,2)) # call with object name
print(Math.add(11, 25)) # even call it with class name