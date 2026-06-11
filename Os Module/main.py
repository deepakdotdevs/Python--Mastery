# Key Points : Os Module in Python

# --------------------------------------------------------------

# Overview : 

# The os module in Python is a built-in library that provides functions for interacting with the
# operating system. It allows you to perform a wide variety of tasks, such as reading and writing
# files, interacting with the file system, and running system commands.

# Here are some common tasks you can perform with the os module:

# Reading and writing files The os module provides functions for opening, reading, and writing files.
# For example, to open a file for reading, you can use the open function:

# import os

# # Open the file in read-only mode
# f = os.open("myfile.txt", os.0_RDONLY)

# # Read the contents of the file
# contents = os.read(f, 1024)

# # Close the file
# os.close(f)

# --------------------------------------------------------------

import os

# if(not os.path.exists("data")):
#     os.mkdir("data") # create a new directory "data" means new folder # 2nd time use when we run with for loop it throws error as directory "data" is already there or created, so we use if

# # now i want to create day 1 to day 100 folder in data, so we do : 
# for i in range(0, 100):
#     os.mkdir(f"data/Day{i+1}")
#     os.mkdir()

# now i want main.py in every day 1 to day 100 folder 

# now i want to rename to Day 1 to Day 100 into tutorial 1 to turotial 100, so we do : 

# for i in range(0,100):
#     os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}")

# now i want to check how many there are tutorial folders exists, for this create oslist.py and there is remaining work : 
