# Key Points : Local & Global Variables in Python : 

# ----------------------------------------------------------------

# Local Variable : Let's say i make an variable in function so can i use it outer of it, noo!! now that's why it is a local variable
# Global Variable : Let's say make a variable out of the function, so can i use it, yess out + inside the function is yess!!

# ----------------------------------------------------------------

# point to remember : global variable not destroyed, local is destroyed itself, local and global variable is differ even of same variable name and the value is not effect other
# if i want x = 5 which is local variable, i want change the value of same variable of global variable x

# x = 4
# print(x)

# def hello():
#     x=5
#     y=1
#     print(f"The local x is {x}")
#     print("hello deepak")

# print(f"The global x is {x}")
# hello()
# print(f"The global x is {x}")
# # print(y) # can't accessable coz it is in local means in function we can access that only in function not outside of that function

# ----------------------------------------------------------------

x= 10 # global variable
def my_function():
    global x # means we want to use variable x which is global variable
    x = 4 # now we change the global in local 
    y = 5 # local variable
    print(y)

my_function()
print(x)
# print(y) # error coz of local var not global