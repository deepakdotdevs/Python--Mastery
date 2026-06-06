# Key Points -> Docstrings & PEP-8

# ----------------------------------------------------------------------

# Python docstrings are the string literals that appear
# right after the definition of a function, method, class,
# or module.

# Whereas,
# Comments are descriptions that help programmers
# better understand the intent and functionality of the
# program. They are completely ignored by the Python
# interpreter.

# ----------------------------------------------------------------------

def square(n):
    '''Takes in a number n, returns the square of n''' # this is the docstring
    print(n**2)
square(5)
# to print the docstring : means docstrings are not ignored as comments
print(square.__doc__)
