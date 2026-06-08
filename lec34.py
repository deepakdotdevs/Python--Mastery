# Key Points : Exception Handling in Python : 

# ---------------------------------------------------------------------

# Exception handling is the process of responding to unwanted or unexpected
# events when a computer program runs. Exception handling deals with these
# events to avoid the program or system crashing, and without this process,
# exceptions would disrupt the normal operation of a program.

# Python has many built-in exceptions that are raised when your program
# encounters an error (something in the program goes wrong).
# When these exceptions occur, the Python interpreter stops the current process
# and passes it to the calling process until it is handled. If not handled, the program
# will crash.

# ---------------------------------------------------------------------

# a = int(input("Enter a Number: "))
# print(f"Multiplication table of {a} is: ")
# for i in range(1,11):
#     print(f"{a} ❌ {i} har= {a*i}")

# if on the place of nos we enter a string then it gives an error, so have to find the solution of this with exception handling

# a = input("Enter a Number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} ❌ {i} = {int(a)*i}")
# except Exception as e:
#     # print(e)  # we can we e as exception printing or this type of another msg also
#     print("Sorry some error occured") # another msgs

# print("Some imp lines of code")
# print("End of program")

# ---------------------------------------------------------------------

# Handle Specific type of error using multiple exceptions : 

try:
    num = int(input("Enter an integer: "))
    a = [6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index Error")
    