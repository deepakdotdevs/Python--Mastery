# Key Points -> Recursion

# ----------------------------------------------------------------------

# We call functions inside the function

# In Python, we know that a function can call other
# functions. It is even possible for the function to call
# itself. These types of construct are termed as recursive
# functions.

# ----------------------------------------------------------------------

# Factorial : 7 = 7*6*5*4*3*2*1 and so on for 1,2,3,4,5,6,7, ----
# Factorial(n) = n*factorial(n-1)

# def factorial(n):
#     if(n==0 or n==1): # Base Condition
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))

# ----------------------------------------------------------------------

# fibonacci series : 

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
# for print first 10 fibonacci Numbers
for i in range(10):
    print(fibonacci(i), end=" ") # end=" " means do no print the next value in next line, instead replace this with a space in same line
    