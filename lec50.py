# Key Points -> map, filter and reduce in python 

# ------------------------------------------------------------

# In Python, the map, filter, and reduce functions are built-in functions that
# allow you to apply a function to a sequence of elements and return a
# new sequence. These functions are known as higher-order functions, as
# they take other functions as arguments.

# ------------------------------------------------------------

# map

# The map function applies a function to each element in a sequence and
# returns a new sequence containing the transformed elements. The map
# function has the following syntax:

# map(function, iterable)

# The function argument is a function that is applied to each element in
# the iterable argument. The iterable argument can be a list, tuple, or any
# other iterable object.

# Program : (i want cube of every item in list means for every item)

# def cube(x):
#     return x*x*x
# print(cube(2)) # output is 8

# # list is : 
# l = [1,2,3,4,5,6,4,2]
# # newl = [] # on the place of these 3 lines we use one line using map
# # for item in l:
# #     newl.append(cube(item))
# # map code line
# newl = map(cube, l) # return map's object
# newl = list(map(cube, l)) # return actual list
# print(newl)

# ------------------------------------------------------------

# filter :

# The filter function filters a sequence of elements based on a given predicate (a
# function that returns a boolean value) and returns a new sequence containing
# only the elements that meet the predicate. The filter function has the following
# syntax:

# filter(predicate, iterable)

# The predicate argument is a function that returns a boolean value and is applied
# to each element in the iterable argument. The iterable argument can be a list,
# tuple, or any other iterable object.

# Program : 

# def cube(x):
#     return x*x*x

# l = [1,3,5,7,6,2] # list used by filter
# newl = list(map(cube,l))
# print(newl)

# # here filter is used : 
# def filter_function(a):
#     return a>3
# newnewl = filter(filter_function, l) # return's filter object
# newnewl = list(filter(filter_function, l))
# print(newnewl)

# ------------------------------------------------------------

# reduce : we have to import it

# The reduce function is a higher-order function that applies a function to a
# sequence and returns a single value. It is a part of the functools module in
# Python and has the following syntax:

# reduce(function, iterable)

# The function argument is a function that takes in two arguments and returns a
# single value. The iterable argument is a sequence of elements, such as a list or
# tuple.

# The reduce function applies the function to the first two elements in the iterable
# and then applies the function to the result and the next element, and so on. The
# reduce function returns the final result.

# from functools import reduce
# # list of nos
# numbers = [1,2,3,4,5]
# # calculate the sum of nos using reduce function
# sum = reduce(lambda x,y:x+y, numbers)
# print(sum)

# ------------------------------------------------------------
