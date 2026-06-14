# Key Points -> Lambda functions in python 

# In Python, a lambda function is a small anonymous function without a name. It is defined using
# the lambda keyword and has the following syntax:

# lambda arguments: expression

# Lambda functions are often used in situations where a small function is required for a short
# period of time. They are commonly used as arguments to higher-order functions, such as map,
# filter, and reduce.

# ------------------------------------------------------------

# def double(x):
#     return x*2
# print(double(5)) # output is 10 

# # using lambda 
# double = lambda x: x*2 # jo ki x leta hai and x*2 return krta hi # func no. 1
# cube = lambda x: x*x*x # func no. 2
# avg = lambda x,y,z: (x+y+z)/3 # func no. 3 with multiple arguments

# print(double(5)) # output is 10 
# print(cube(5)) # output is 125
# print(avg(3,5,10)) # 6.0

# ------------------------------------------------------------

# use function as a argument, program example means function mein function pass kr skte hai : 

# def appl(fx, value):
#     return 6+fx(value)
# cube = lambda x: x*x*x
# print(appl(cube, 2)) 
# # we can also write it as : 
# print(appl(lambda x: x*x*x, 2)) # anonyms function means without name

# ------------------------------------------------------------

# Program No. 3 : 

# multiple=lambda x,y: print(f"{x} * {y} = {x*y}")
# print(multiple(2,3))

# ------------------------------------------------------------
