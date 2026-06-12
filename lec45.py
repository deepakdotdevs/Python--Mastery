# Key Points -> Filo IO in python, Part - I

# --------------------------------------------------------------

# File handling like read, write, append : 
# The methods are built-in in python for files.

# Modes in file :

# There are various modes in which we can open files :

# 1. read (r): This mode opens the file for reading only
# and gives an error if the file does not exist. This is the
# default mode if no mode is passed as a parameter.
# 2. write (w): This mode opens the file for writing only
# and creates a new file if the file does not exist.
# 3. append (a): This mode opens the file for appending
# only and creates a new file if the file does not exist.
# 4. create (x): This mode creates a file and gives an error
# if the file already exists.
# 5. text (t): Apart from these modes we also need to
# specify how the file must be handled. t mode is used
# to handle text files. t refers to the text mode. There is
# no difference between r and rt or w and wt since text
# mode is the default. The default mode is 'r' (open for
# reading text, synonym of 'rt' ).

# --------------------------------------------------------------

# Opening a File

# Before we can perform any operations on a file, we must first open it. Python
# provides the open( function to open a file. It takes two arguments: the name of
# the file and the mode in which the file should be opened. The mode can be 'r' for
# reading, 'w' for writing, or 'a' for appending.

# Here's an example of how to open a file for reading:

# f = open('myfile.txt', 'r')

# By default, the open() function returns a file object that can be used to read from
# or write to the file, depending on the mode.

# Program : 

# f = open('myfile.txt', 'r') # For open # if file doesn't exists gives error, if i open this file in write mode means 'r' is replaced by 'w' the file is can't be abstracted
# # f = open('myfile.txt') # if we executes it, it's works coz r mode is by default in python
# print(f)
# text = f.read() # For print out the content which is present in file
# print(text) # for print the content which is present in the file
# f.close()

# --------------------------------------------------------------

# w -> for write in file, even if file is not exists it automatically creates it, if we write using this then the content which is present already in file is delte and then write

# f = open('myfile2.txt', 'w') # creates automatically as it's not exists in the folder

# --------------------------------------------------------------

# a = append, means i want to write in the end of the content which is already exists in the file without delete content which is already present in file

# --------------------------------------------------------------

# x = create, this mode creates a file and gives an error if the file is already exists

# --------------------------------------------------------------

# t : 

# f = open('myfile.txt', 'rt') # r means read and t means text mtlb mein file ko as a text file open krna chayata hu, by the way t is by default in python 

# # but if we replace it with b : 
# f = open('myfile.txt', 'rb') # means open the file in the binary format, mtlb jo content hoga jo binary mein aayega

# --------------------------------------------------------------
