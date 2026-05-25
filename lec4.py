# Key Concepts -> Comments, Escape Sequence & Print Statement

# Comments -> In computer programming, comments are human-readable notes embedded within the source code to explain what the code is doing. These notes are ignored by the compiler or interpreter, meaning they have no effect on how the program actually runs.
# This is a comment
# Multi line comment is also possible -> select text for comment out and ctrl+/
# and also using the single/double quotes -> ''' text ''' or """ text """

""""
This
is
a multi line
comment
"""
# ------------------------------------------------------------------------

print("Hey i am a good boy\nand this viewer is also a good boy/girl") # For next line (this is the comment after inline code)

# \n is a newline character. It is a special escape sequence 

# ------------------------------------------------------------------------

# Escape Sequence Characters : 
# i) to insert a character in a string

print("Hey I\'am a \"good boy\"\nand this viewer is also a good boy/girl")

# ----------------------------------------------------------------------------

# Multiple Values in print : 
# Seperator -> "~" or "-" any symbol
# Default Seperator is "space"
# end is the what to print at the end

print("hey", 6, 7, sep="~", end="009\n")
print("Deepak")