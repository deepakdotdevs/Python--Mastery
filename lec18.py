# Key Points -> Functions in Python 

# We'd like to use our code's logic multiple times, there we use function

# ---------------------------------------------------------------------

# A function is a block of code that performs a specific task whenever it is called. In
# bigger programs, where we have large amounts of code, it is advisable to create
# or use existing functions that make the program flow organized and neat.

# There are two types of functions:

# 1. Built-in functions -> functions are defined and pre-coded in python. Examples: min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print() etc
# 2. User-defined functions -> we can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

# ---------------------------------------------------------------------

# a = 9
# b = 8
# gmean1 = (a*b)/(a+b) # gmean = geometric mean
# print(gmean1)
# c =8
# d = 7
# gmean = (c*d)/(c+d) # gmean of c and d

# print(gmean)

# as there we have to use formula multiple times for multiple values, therefore we use there functions

# Updated Program code with function :

# def calculateGmean(a,b): # def if used to define function, calculateGmean is function's name and a and b is arguments
#     mean = (a*b)/(a+b)
#     print(mean)
# # Now,
# a = 9
# b = 8
# calculateGmean(a ,b)
# c = 8
# d = 7
# calculateGmean(c, d)

# 2nd Program : 

# def greaterNum(a, b):
#     if(a>b):
#         print("Greater Number is ", a)
#     else:
#         print("Greater Number is ", b)
# a = 5
# b = 10
# c = 18
# d = 17
# greaterNum(a, b)
# greaterNum(c, d)

# ---------------------------------------------------------------------

def isLesser(a ,b):
    pass # pass means you have to do nothing coz i make it's body later