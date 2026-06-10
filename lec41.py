# Key Points : How import works in Python .?

# ---------------------------------------------------------------------------------------

# How importing in python works ? 

# Importing in Python is the process of loading code from a Python module into the current script.
# This allows you to use the functions and variables defined in the module in your current script, as
# well as any additional modules that the imported module may depend on.

# To import a module in Python, you use the import statement followed by the name of the module.
# For example, to import the math module, which contains a variety of mathematical functions, you
# would use the following statement:

# import math

# Once a module is imported, you can use any of the functions and variables defined in the module
# by using the dot notation. For example, to use the sqrt function from the math module, you would
# write:

# import math

# result = math.sqrt(9)
# print(result) # Output: 3.0

# --------------------------------------------------------------------------------------


# import math

# ans=math.floor(4.2343)
# print(ans)

# import math
# result = math.sqrt(9)
# print(result)

# from math import sqrt, pi
# result =sqrt(9)*pi # directly use
# print(result)

# To import everything :

# It's also possible to import all functions and variables from a module using the * wildcard.
# However, this is generally not recommended as it can lead to confusion and make it harder to
# understand where specific functions and variables are coming from.


# Python also allows you to rename imported modules using the as keyword. This can be useful if
# you want to use a shorter or more descriptive name for a module, or if you want to avoid naming
# conflicts with other modules or variables in your code.

# from math import *
# result = sqrt(9)*pi
# print(result)



# --------------------------------------------------------------------------------------

# The "as" keyword :

# import math as s # import as a variable 
# result = s.sqrt(9)
# print(result)
# print(s.pi)

# # from math import pi, sqrt as s
# import math as m
# result = m.sqrt(9)*m.pi
# print(result)

# --------------------------------------------------------------

# Finally, Python has a built-in function called dir that you can use to view the names of all the
# functions and variables defined in a module. This can be helpful for exploring and understanding
# the contents of a new module.

# import math

# print(dir(math))

# This will output a list of all the names defined in the math module, including functions like sqrt and
# pi, as well as other variables and constants.

# In summary, the import statement in Python allows you to access the functions and variables
# defined in a module from within your current script. You can import the entire module, specific
# functions or variables, or use the * wildcard to import everything. You can also use the as keyword
# to rename a module, and the dir function to view the contents of a module.

# import math
# print(dir(math))
# print(math.nan, type(math.nan))

# --------------------------------------------------------------


# Program Question : 

# create a new python file "deepak.py" and enter some lines of code : 
# def welcome():
#     print("Hey you are welcome my friend")
# deepak = "a good boy"

# Now, here part : 

# from deepak import welcome, deepak
# # from deepak import * # to import everything from deepak's file
# welcome()
# print(deepak)

# import deepak as dee
# dee.welcome()
# print(dee.deepak)

# --------------------------------------------------------------
