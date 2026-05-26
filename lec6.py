# Operators : 
# + Addition 15+7
# - Subtraction 15-7
# * Multiplication 15*7
# / Division 15/7
# % Modulus 15%7
# // Floor Division 15//7
# ** Exponential 5**3

print(15+7)
print(15-7)
print(15*7)
print(15/7)
print(15%7)
print(15//7)
print(5**3)

# --------------------------------------------------

# Create a calculator capable of performing addition, subtraction, multiplication and division
# operations on two numbers. Your program should format the output in a readable manner!

nums1 = 50
nums2 = 100
addition = nums1+nums2
subtraction = nums1-nums2
multiplication = nums1*nums2
division = nums1/nums2
floorDivision = nums1//nums2
exponential = nums1**nums2
modulus = nums1%nums2
print("Value of ", nums1, " + ", nums2, " = ", nums1+nums2)
print("Value of ", nums1, " - ", nums2, " = ", nums1-nums2)
print("Value of ", nums1, " * ", nums2, " = ", nums1*nums2)
print("Value of ", nums1, " / ", nums2, " = ", nums1/nums2)
print("Value of ", nums1, " // ", nums2, " = ", nums1//nums2)
print("Value of ", nums1, " ** ", nums2, " = ", nums1**nums2)
print("Value of ", nums1, " % ", nums2, " = ", nums1%nums2)