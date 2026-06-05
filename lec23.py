# Key Points -> Tuple Methods : 

# ---------------------------------------------------------------------

# Tuples are immutable, hence if you want to add, remove or change tuple
# items, then first you must convert the tuple to a list. Then perform operation
# on that list and convert it back to tuple.

# ---------------------------------------------------------------------

# countries = ("A", "B", "D", "E", "F", "G", "H")
# temp = list(countries) # tuple into list
# temp.append("New Country")
# print(temp)
# temp.pop(3) # remove value on this index no.
# print(temp)
# temp[2] = "Updated" # change or update the value
# print(temp)
# countries = tuple(temp) # Convert List into tuple
# print(countries, type(countries)) # print type and whole updated tuple

# ---------------------------------------------------------------------

# We can directly concatendate two tuples without converting them to list ;

# tup1 = (1,2,3,4,5)
# tup2 = (6,7,8,9,10)
# tup3 = tup1+tup2
# print(tup3)

# ---------------------------------------------------------------------

# count() : how many occurences of given value in a tuple

tup = (1,2,3,7,5,6,3,6,5,9,7,1)
res = tup.count(6)
print(res)

# index() : return the 1st occurence's index no. of the given element, raise valueerror when there is no exact value 

tup2 = (8,7,4,5,6,1,2,0,3,4,5,6,7,8,9)
res2 = tup2.index(1)
print(res2)

# if i want in a portion occurence of given no. threw index() then we have to do ..!!
# syntax of index() => index(element, start, end)
res3 = tup2.index(4, 4, 10)
print(res3)

# for length of tuple
res3 = len(tup2)
print(res3)
