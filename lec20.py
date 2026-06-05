# Key Points -> List : 

# ----------------------------------------------------------------

# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation.
# We can use different data types in one list and it is mutable.

# ----------------------------------------------------------------

# marks = [3,5,6, 7, 8, 9, "Deepak", "Marks"]
# print(marks) # print the list
# print(type(marks))
# print(marks[0]) # accessing element from index, indexing stars from 0
# print(marks[1])
# print(marks[2])
# print(len(marks)) # is 3 means starts from 1
# # Negative indexing
# print(marks[len(marks)-3]) # is 7 from end (starts from 1 from end 1, 2, 3, ---)
# print(marks[6])
# print(marks[7])
# print(marks[8]) # list index out of range gives an error

# ----------------------------------------------------------------

# if i want to check that element is exists in list or not, then ..

# marks = [3,4,5,6,7,8]
# if 9 in marks:
#     print("yes")
# else:
#     print("no")

# # same concept is exists for String :

# name = "Deepak"
# if "eep" in "Deepak": # try pak, Dee, pak etc also
#     print("yes")
# else:
#     print("no")

# ----------------------------------------------------------------

# wants to print all elements of the list : 

# marks = [4,5,6,7,8,9, "pel", "eos"]
# print(marks) # print all the list
# print(marks[:]) # print all the list
# print(marks[1:]) # from index 1 to last
# print(marks[:4]) # from 0 to 3rd index as 4 means takes to 3rd index element
# print(marks[1:-1]) # means 1:len(marks)-1 means 1:8-1 => 1:7 means 5 to "pel"

# ----------------------------------------------------------------

# Jump Index : 

# You can print a range of list items by specifying where you want to start,
# where do you want to end and if you want to skip elements in between
# the range.

# marks = [1,2,3,4,5,6,7,8,9, 10]
# print(marks[1:8:2]) # 2 is jump index means takes 1st then skip first and print 2nd and so on # it's output is => 2,4,6,8
# print(marks[1:9:3]) # output is => 2,5,8

# ----------------------------------------------------------------

# List Comprehension : 

# Program No. 1 : 

# Lst = [i for i in range(4)] # means starting index is 0 and last is 4 which prints from 0 to 3 indexes
# print(Lst) # [0,1,2,3]
# Lst2 = [i*i for i in range(4)]
# print(Lst2) # [0,1,4,9]
# Lst3 = [i*i for i in range(10) if i%2==0]
# print(Lst3) # (0, 2, 4, 6, 8) ka square

