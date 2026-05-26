# Key Topic is -> Typecasting

# The conversion of one data type into the other data type is known as type casting in python or type
# conversion in python.
# Python supports a wide variety of functions or methods like: int(), float0, strO, ord0, hex0, oct0,
# tuple0, set0, list0, dict0, etc. for the type casting in python.

a = "1"
b = "2"
print(int(a)+int(b))

# ------------------------------------------------------------------------------------------------------

# Two Types of Typecasting:

# 1. Explicit Conversion (Explicit type casting in python) -> Manually
# 2. Implicit Conversion (Implicit type casting in python) -> Automatically

# Explicit typecasting:
# The conversion of one data type into another data type, done via
# developer or programmer's intervention or manually as per the
# requirement, is known as explicit type conversion.
# It can be achieved with the help of Python's built-in type
# conversion functions such as int0, float0, hex0, oct0, str0, etc.

str = "15"
num = 7
str_num = int(str)
sum = str_num+num
print(sum)

# Implicit type casting:
# Data types in Python do not have the same
# level i.e. ordering of data types is not the
# same in Python. Some of the data types
# have higher-order, and some have lower
# order. While performing any operations on
# variables with different data types in
# Python, one of the variable's data types will
# be changed to the higher data type.
# According to the level, one data type is
# converted into other by the Python
# interpreter itself (automatically). This is
# called, implicit typecasting in python.

# Python converts a smaller data type to a
# higher data type to prevent data loss.

c = 7
d = 25.04
print(c+d)