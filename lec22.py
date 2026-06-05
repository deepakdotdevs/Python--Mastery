# Key Points -> Tuples : 

# ---------------------------------------------------------------------

# It is not mutable means imutable not changable and similar to list and use Parantheses ()

# Tuples are ordered collection of data items. They store multiple items in a single
# variable. Tuple items are separated by commas and enclosed within round brackets
# (). Tuples are unchangeable meaning we can not alter them after creation.

# ---------------------------------------------------------------------

# tup = (1,5,6)
# print(type(tup))
# print(tup)
# # if there is only one element in tuple. Eg;
# tup1 = (1,) # it gives us class type of int as there is only one integer value and to tuple we have to use comma "," after that one value then it gives us output of class is tuple
# print(type(tup1))

# # tup[0] = 30 # gives error as it is immutable and this type of syntax is of list

# tup3 = (1,2,3,4,5, "Deepak", 'Sahdev', True, False)
# print(type(tup3), tup3)
# print(tup3[0])
# print(tup3[1])
# print(tup3[2])
# print(tup3[3])
# print(tup3[4])

# ---------------------------------------------------------------------

# Positive/Negative Indexing and jump is exactly same as in List.

# ---------------------------------------------------------------------

tup = (1,2,3,4,5,6,7,8,9, "Deepak", 'A', 'ABC')
if 4 in tup:
    print("Yes")
else:
    print("Noo!!")

# Slicing (make a new tuple) : 
tup2 = tup[1:4:2]
print(tup2)

# ---------------------------------------------------------------------

tup2[0:len(tup2)]
