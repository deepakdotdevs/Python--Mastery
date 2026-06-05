# Key Points -> List Methods in Python : 

# ----------------------------------------------------------------

# append() : TO add element in the end of the list :

# l = [1,2,3,4,5]
# print(l)
# l.append(7)
# print(l)

# ----------------------------------------------------------------

# list.sort() and list.sort(reverse=True) : To sort list in ascending/descending order : 

# l = [45, 34, 76, 34, 1,2,3,4,5,4,3,3,2,2]
# l.sort() # ascending order
# print(l)
# l.sort(reverse=True) # descending order
# print(l)

# ----------------------------------------------------------------

# reverse() : Original list's opposite :

# l = [7,6,5,4,3,4,5,6,7,6,5,4,3]
# l.reverse()
# print(l)

# ----------------------------------------------------------------

# index() : returns index no. at which index the element is exists in list

# l = [6,5,4,3,2,1]
# print(l.index(3))

# ----------------------------------------------------------------

# count() : which element how many times is exists in the list

l = [1,2,3,4,5,6,7,8,9,1,2,3,1,2,3,4,5,6,5,1,2,3,1]
print(l.count(1))

# ----------------------------------------------------------------

# copy() : 

# 1st Program without copy() :

# l = [11,45,1,2,4,6,1,1]
# m = l
# m[0] = 0
# print(l) # makes also changes in the l list with m list, it create problem therefore, we use there copy() by which the original list is can't changed

# 2nd Program with copy() : 

l = [1,2,3,4,5,4,3,21,2]
m = l.copy()
m[0] = 0
print(l) # prints original list 
print(m) # prints m list which is the copy of the l list

# ----------------------------------------------------------------


