# Key Points -> 'is' vs '==' in python 

# ------------------------------------------------------------

# is is for exact location of object in memory
# == is for values (is object's value is same or not)
# Both are comparision operators

# ------------------------------------------------------------

# a =[1,2,43] #3 both are true
# b=[1,2,43] #3 both are true if value is 3 for both
# print(a is b) # exact location of object in memory
# print(a==b) # value

a=(1,2)
b = (1,2)
print(a is b)
print(a==b)

a=None
b = None
print(a is b)
print(a is None)
print(a==b)
