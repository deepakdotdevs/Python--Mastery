# Key Points : f string in python

# ----------------------------------------------------------------------

# It is a new string formatting mechanism introduced by the PEP 498. It
# is also known as Literal String Interpolation or more commonly as F-
# strings (f character preceding the string literal). The primary focus of
# this mechanism is to make the interpolation easier.

# When we prefix the string with the letter 'f', the string becomes the f-
# string itself. The f-string can be formatted in much same as the
# str.format0 method. The f-string offers a convenient way to embed
# Python expression inside string literals for formatting.

# ----------------------------------------------------------------------

# Old Method of string formating, but it is not convencing : 

# letter = "Hey my name is {} and I am from {}"
# country = "India"
# name = "Deepak"
# letter.format(name, country)
# print(letter.format(name, country)) # that's right order
# print(letter.format(country, name)) # wrong order and that's why we also represent threw the nos 
# letter = "Hey my name is {1} and I am from {0}"
# print(letter.format(country, name)) # as country index's is 0 and name index is 1

# ----------------------------------------------------------------------

# New method : We use f-string means we can use variable in our string

# letter = "Hey my name is {} and I'm from {}"
# name = "Deepak"
# country = "India"
# print(f"My name is {name} and I'm from {country}")

txt = "for only {price: .2f} dollars!" # .2f means takes only 2 decimal places
print(txt.format(price = 49.025884))

# Using f-string 2nd program becomes
price = 24.0999999
print(f"For only {price: .2f} dollars")
# OR
txt = f"For only {price: .2f} dollars!"
print(txt)

print(f"{2*30}") # Output is as a string
print(type(f"{2*30}"))

# ----------------------------------------------------------------------

# we want to print literally {} in f-string without the value then the program is : 

print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
