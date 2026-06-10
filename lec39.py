# Key Points : Enumerate Function in Python :

# ---------------------------------------------------------------

# Without Enumerate Function : We have to define index, and etc etc more details :

# The enumerate function is a built-in function in Python that allows
# you to loop over a sequence (such as a list, tuple, or string) and get
# the index and value of each element in the sequence at the same
# time. Here's a basic example of how it works:

# ---------------------------------------------------------------


# marks = [34,23,12,43,54,65,86,45]
# index =0
# for mark in marks:
#     print(mark)
#     if(index==6):
#         print("Deepak awesome!")
#     index += 1

# With Enumerate Function : 

marks = [34,23,12,43,54,65,86,45]
for index, mark in enumerate(marks):
    print(mark)
    if(index==6):
        print("Deepak awesome!")