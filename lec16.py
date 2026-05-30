# Key Point -> While Loop : 

# As the name suggests, while loops execute statements while
# the condition is True. As soon as the condition becomes False,
# the interpreter comes out of the while loop.

# -----------------------------------------------------------------

# first we define the variable : 

# i = 0
# while(i<=3):
#     print(i)
#     i = i+1 # condition of iteration
# print("Done with the loop")

# -----------------------------------------------------------------

# i = int(input("Enter the number: "))
# while(i<=38):
#     i = int(input("Enter the number: "))
#     print(i)
# print("Done with the loop")

# -----------------------------------------------------------------

# Decrement loop : 

# i = 10
# while(i>0):
#     print(i)
#     i = i-1

# -----------------------------------------------------------------

# Else with while loop : 
# i=5 # if i = -5 then else is directly executed
# while(i>0):
#     print(i)
#     i = i-1
# else:
#     print("Else statement is executed") # as soon as while loop become false, else is executed

# -----------------------------------------------------------------

# there is no do-while loop in python, example of C++ or in Java : atleast one time executed even true or false condition

# do {
#     # loop body
# }while(condition)

# But we can execute it using while loop : 

while True:
    num = int(input("Enter a number greater than 10: "))
    if(num>10):
        print("valid Number")
        break
    print("Number Smaller than 10 is ", num)
