# Key Points : Finally keyword in python : 

# ---------------------------------------------------------------------

# It's is executes whether the error is come or not, it's always executes itself with an custom msg : 

# The finally code block is also a part of exception handling. When we handle exception
# using the try and except block, we can include a finally block at the end. The finally
# block is always executed, so it is generally used for doing the concluding tasks like
# closing file resources or closing database connection or may be ending the program
# execution with a delightful message.
# ---------------------------------------------------------------------

# def func1():
#     try:
#         l = [1,2,3,4,5]
#         i = int(input("Enter the index: "))
#         print(l[i])
#         return 1
#     except:
#         print("Some error occurred")
#         return 0
#     print("I'm always executed") # it's is not executed there, and hence we have to use finally keyword

# x = func1()
# print(x)

# def func1():
#     try:
#         l = [1,2,3,4,5]
#         i = int(input("Enter the index: "))
#         print(l[i])
#         return 1
#     except:
#         print("Some error occurred")
#         return 0
#     finally:
#         print("I'm always executed")
# x = func1()
# print(x)

# ---------------------------------------------------------------------

