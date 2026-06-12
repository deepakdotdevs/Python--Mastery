# Key Points : File IO in Python,  Writing to a file, appending & with statement : 

# --------------------------------------------------------------

# f = open('myfile.txt', 'w') # past content is deleted and new is added
# f.write('Hello, world!')
# f.close()

# in append mode : past content is exactly same no delete and add new data 

# f = open('myfile.txt', 'a')
# f.write('Hello, world!!')
# f.close()

# --------------------------------------------------------------

# The 'with' statement

# Alternatively, you can use the with
# statement to automatically close
# the file after you are done with it.

# Program : 

with open('myfile.txt', 'a') as f:
    f.write("Hey I'm inside with") # f.close() is automatically work with this method