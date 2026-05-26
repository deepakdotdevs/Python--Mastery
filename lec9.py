# Key Point -> String

# ---------------------------

# String can be enclosed in "" double quotes, '' single quotes, ''' also """" triple quotes for multi line string

name = "Deepak"
friend = "Sahdev Sharma"
anotherFriend = 'Kushagra'
stringLine = "He said, \"I want to eat an apple\""
stringLine2 = '''He said, "I want to eat an apple"'''
stringMultiLine = '''He said,
Hi Deepak
hey I'm Good'''
stringMultiLine2 = """
Note: It does not matter whether you enclose your strings in single or double
quotes, the output remains the same.

Sometimes, the user might need to put quotation marks in between the strings.
Example, consider the sentence: He said, "I want to eat an apple".

How will you print this statement in python ?: He said, "I want to eat an
apple". We will definitely use single quotes for our convenience

print('He said, "I want to eat an apple".')
"""

print(name)
print(friend)
print(anotherFriend)
print(stringLine)
print(stringLine2)
print(stringMultiLine)
print(stringMultiLine2)

# ---------------------------------------------------------------

# indexing is start from 0 and we use to print the characters of a string

str = "DEEPAK"
print(str[0])
print(str[3])
print(str[5])
# print(str[6]) # throws an error, as index is out of bound

# Using for loop we can print all of the characters of an string
print("Let's Use a for loop\n")
for character in friend:
    print(character)