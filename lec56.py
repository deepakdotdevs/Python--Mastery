# Key Points : Decorators in Python (Basically those functions who change other functions and then return them)

# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and
# methods. They are a way to extend the functionality of a function or method without modifying its source code.

# A decorator is a function that takes another function as an argument and returns a new function that modifies the
# behavior of the original function. The new function is often referred to as a "decorated" function. The basic syntax
# for using a decorator is the following:

# @decorator_function
# def my_function():
# pass

# The @decorator_function notation is just a shorthand for the following code:

# def my_function():
# pass
# my_function = decorator_function(my_function)

# Decorators are often used to add functionality to functions and methods, such as logging, memoization, and
# access control.

# ----------------------------------------------------------------------
# Let's say i want it's says welcome before start main execution and also thank you after the execution : 

def greet(fx): # it's a decorator
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function!!")
    return mfx
@greet 
# # 2nd option call hello function with greet as show in below down.
def hello():
    print("Hello World!!")

def add(a,b):
    print(a+b)
greet(hello)()
hello()

# ----------------------------------------------------------------------

# Practical use case

# One common use of decorators is to add logging to a function. For
# example, you could use a decorator to log the arguments and return
# value of a function each time it is called:

# import logging

# def log_function_call(func):
# def decorated(*args, ** kwargs):
# logging. info(f"Calling {func .__ name_} with
# args={args}, kwargs={kwargs}'N
# result = func(*args, ** kwargs)
# logging. info(f"{func .__ name_} returned
# {result}")
# return result
# return decorated

# @log_function_call
# def my_function(a, b):
# return a + b

# In this example, the log_function_call decorator takes a function as
# an argument and returns a new function that logs the function call
# before and after the original function is called.

# Program :

def greet(fx): 
    def mfx(*args, **kwargs): # *args takes all arguments as tuple and **kwargs as dictionary
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function!!")
    return mfx
@greet 
def hello():
    print("Hello World!!")
@greet
def add(a,b):
    print(a+b)
# greet(hello)()
hello()
greet(add)(1,2) # arguments required for it we *args, **kwargs in mfx function
add(4,5) # normally calling function

# ----------------------------------------------------------------------

# Program : 

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated
@log_function_call
def my_function(a,b):
    return a+b

