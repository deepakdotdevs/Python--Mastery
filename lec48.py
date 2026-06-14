# Key Points -> File IO -> seek(), tell() and other functions

# ------------------------------------------------------------

# In Python, the seek() and tell() functions are used to work with file
# objects and their positions within a file. These functions are part of
# the built-in io module, which provides a consistent interface for
# reading and writing to various file-like objects, such as files, pipes,
# and in-memory buffers.

# seek() function : Using file is myfile6.txt

# The seek0 function allows you to move the current position within a
# file to a specific point. The position is specified in bytes, and you can
# move either forward or backward from the current position. For
# example:

# with open('myfile6.txt', 'r') as f:
#     print(type(f))
#     f.seek(10) # move to the 10th byte in the file
#     data = f.read(5) # read the next 5 bytes
#     print(data)

# ------------------------------------------------------------

# tell() : Using file (kaha pr seek kra hua hai ye pta Lga skte hai or )

# The tell() function returns the current position within the
# file, in bytes. This can be useful for keeping track of your
# location within the file or for seeking to a specific position
# relative to the current position. For example:

# with open('myfile6.txt', 'r') as f:
#     print(type(f))
#     f.seek(10) # move to the 10th byte in the file
#     print(f.tell()) # tell us ki kaha tk hmne seek kra hua hai file mein
#     data = f.read(5) # read the next 5 bytes
#     print(data)

# ------------------------------------------------------------

# trucate() : Using file is "myfile7.txt" : 

# When you open a file in Python using the open function, you
# can specify the mode in which you want to open the file. If
# you specify the mode as 'w' or 'a', the file is opened in write
# mode and you can write to the file. However, if you want to
# truncate the file to a specific size, you can use the truncate
# function.

# mtlb meri file mein mene write krva diya hai, 
# lekin i want ki file ka size sirf 5 characters hi ho

# with open('myfile7.txt', 'w') as f:
#     f.write('Hello World!')
#     f.truncate(5) # test is also by comment it
# with open('myfile7.txt', 'r') as f:
#     print(f.read())

# ------------------------------------------------------------

