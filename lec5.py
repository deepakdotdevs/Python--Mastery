# Key Points : Variables & Data Types
# In python everything is object like data types etc everything
# -----------------------------------------------------------------------

# a variable is a container used to store data or values.
# It helps us save information that can be used later in the program.
# variables are used :
# Store data
# Reuse values
# Make programs dynamic
# Reduce repeated code

a = 5758 # a is variable
print(a)
b = "Deepak" # b is variable
print(b)
c = True
d = None

# -----------------------------------------------------------------------

# Data type specifies the type of value a variable holds. This is required in
# programming to do various operations without causing an error.
# In python, we can print the type of any operator using type function:

e = 10
print(type(a))
f = "plm"
print(type(f))

g = 123
g1 = 8
print(g+g1)
print("Type of g is", type(g))
print("Type of g1 is", type(g1))
print("Type of c is", type(c))
print("Type of d is", type(d))

# -----------------------------------------------------------------------

# Built-In Data Type : -> 

# i) Numerica data: int, float, complex :

# · int: 3, -8, 0
a2 = 458 # this is a int
print(type(a2))
# · float: 7.349, -9.0, 0.0000001
a3 = 45.02 # this is a float data type
print(type(a3))
# · complex: 6 + 2i
a4 = complex(8, 2)
print(a4)
print(type(a4))

# ii) Text data: str
str = ("Hello World!!!")
print(str)
print(type(str))

# iii) Boolean data: True or False
# Boolean data consists of values True or False

# iv) Sequenced data: list, tuple

# list -> List is basically a collection of different data elements jo ki alag alag data types ke bhi ho skte hai, and we can make changes in list, means it is mutable, use square brackets
list1 = [8, 2.1, [-4,5], ["apple", "banana"]]
print(list1)
print(type(list1))

# Tuple -> Exactly same as list but we can't make changes in the tuple, means it is immutable, uses parentheses
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"), 1,2,3, (4,5,6, "plm"))
print(tuple1)
print(type(tuple1))

# v) Mapped data: dict (dictionery)
# A dictonary is an unordered collection of data containing a key:value pair, The key-value pairs are enclosed within curly brackets
dict1 = {"name":"Deepak", "age":20, "canVote":True}
print(dict1)
print(type(dict1))

# ------------------------------------------------------------------------------------------------------------------------