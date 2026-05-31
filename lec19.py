# Key Points -> Function Arguments : 

# -----------------------------------------------------------------------

# There are four types of arguments that we can provide in a function : 
# Default Arguments
# Keyword Arguments
# Variable length Arguments
# Required Arguments

# -----------------------------------------------------------------------

# Simple Program or this is the Required Arguments in this case : 

# def average(a, b):
#     print("The average is ", (a+b)/2)
# average(5, 18)

# default argument program : 

# def average(a=9, b=1):
#     print("The average is ", (a+b)/2)
# average() # it will work and take the default values from the arguments already defined as 9 and 1
# average(20, 30) # in this it will ignore the default values as we provide in the function here
# average(99) # this take a = 99 and b = 1
# average(b= 45) # this takes a = 9 and b = 45

# nd program of default argument : 

# def name(fname, mname = "Jangid", lname = "Yograj"):
#     print("Hello, ", fname, mname, lname)
# name("Deepak")
# name("Deepak", lname = "Sharma")
# name("Deepak", mname ='Gupta')

# -----------------------------------------------------------------------

# Keyword Argument program : 

# We can provide arguments with key = value, this way the
# interpreter recognizes the arguments by the parameter name.
# Hence, the the order in which the arguments are passed does
# not matter.

# program : 

# def name(fname, mname, lname):
#     print("Hello, ", fname, mname, lname)
# name(mname = "Jangid", fname = "Deepak", lname = "Yograj")

# -----------------------------------------------------------------------

# Required Argument : 

# def name(fname, mname = "pot", lname = "qer"):
#     print("Hello,", fname, mname, lname)
# name("Deepak") # here is Deepak is required argument as we can't skip this argument in any condition

# -----------------------------------------------------------------------

