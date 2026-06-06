# Key Points : Set Methods : 

# ---------------------------------------------------------------------

# combination of two sets means joining of sets or we Say Union of Set (means merging of 2 sets) : 

# s1 = {3,5,8}
# s2 = {5,7,8}
# print(s1.union(s2))

# # update()
# print(s1, s2) # not updated 
# s1.update(s2) # means take s2 values in s1
# print(s1, s2)
 
# intersection and intersection update() : 

# cities = {"tokyo", "madrid", "Berlin", "Delhi"}
# cities2 = {"tokyo", "seoul", "kabul", "madrid"}
# # cities3 = cities.intersection(cities2) # which is in both sets
# # print(cities3)
# cities.intersection_update(cities2) # makes the cities updated with intersection values
# print(cities)

# ---------------------------------------------------------------------

# Symmetric Difference : (AUB) - (A intersection B) : means all values which are not common 


# s1 = {1,2,3,4,5}
# s2 = {1,7,3,8,5}
# s3 = s1.symmetric_difference(s2)
# print(s3)

# ---------------------------------------------------------------------

# difference

# s1 = {1,2,3,4,5}
# s2 = {3,4,5,6,7,8,9}
# s3= s1.difference(s2)
# print(s3)

# ---------------------------------------------------------------------

# isdisjoint() : 

# The isdisjoint() method checks if items of given set are present in
# another set. This method returns False if items are present, else it
# returns True. means intersection completely must be 0

# s1 = {1,2,3} # return false when even one element is same to another set
# s2 = {4,5,6,7,8,9}
# print(s1.isdisjoint(s2))

# ---------------------------------------------------------------------

# issuperset() : 

# kya cities superset hai cities2 ka means kya cities2 ke sabhi elements cities mein already hai ya nahi: 

# cities = {"tokyo", "madrid", "berlin", "delhi"} # for False
# # cities = {"tokyo", "madrid", "seoul", "kabul", "berlin", "delhi"} # for True
# cities2 = {"seoul", "kabul"}
# print(cities.issuperset(cities2))

# ---------------------------------------------------------------------

# issubset() : Opposite of the issuperset()

# s1 = {1,2,3,4,5}
# s2 = {1,2,3,4,5,6,7,8,9}
# print(s1.issubset(s2))

# ---------------------------------------------------------------------

# add() : If you want to add a single item to the set use the add() method.

# s1 = {1,2,3,4,5}
# s1.add(6) # we can only add one element or value at a time
# print(s1)

# ---------------------------------------------------------------------

# update : If you want to add more than one item

# s1 = {1,2,3,4,5}
# s2 = {5,6,7,8}
# s2.update(s1)
# print(s2)

# ---------------------------------------------------------------------

# remove()/distract() : We can use remove() and distract() methods to remove items from set

# The main difference between remove and discard is that, if we try
# to delete an item which is not present in set, then remove0 raises
# an error, whereas discard( does not raise any error.

# s1 = {1,2,3,4,5}
# s1.discard(6)
# s1.remove(4)
# print(s1)

# ---------------------------------------------------------------------

# pop() : 

# This method removes the last item of the set but the catch is that
# we don't know which item gets popped as sets are unordered.
# However, you can access the popped item if you assign the pop()
# method to a variable.

# s1 = {1,2,3,4,5}
# s1.pop() # as set are unordered, we don't know which element is remove by pop()
# print(s1)

# ---------------------------------------------------------------------

# del() : del is not a method, rather it is a keyword which deletes the set entirely

# cities = {"A", "B", "C", "D", "E", "F"}
# del cities
# print(cities) # gives error as cities is not defined coz it it entirely deleted

# ---------------------------------------------------------------------

# clear() : this method clears all items in the set and prints an empty set, means not delete the set entirely

# s1 = {1,2,3,4,5,6}
# s1.clear()
# print(s1)

# ---------------------------------------------------------------------

# last problem : 

# info = {"carla", 19, False, 5.9}
# if "carla" in info:
#     print("Yes")
# else:
#     print("No!!")

# ---------------------------------------------------------------------
