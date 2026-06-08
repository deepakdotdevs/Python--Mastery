# Key Points : For loop with else in python :

# ---------------------------------------------------------------------

# Is else statement is only used with if or we can use it with for loop too - answer is yes. That's how : 

# for i in range(5): # it prints 1 to 4 and then 5 is not executed, therefore it goes to else condition and prints Sorry no i
#     print(i)
# else:
#     print("Sorry no i")

# for i in []: # empty list, that's why prints Sorry no i directly
#     print(i)
# else:
#     print("Sorry no i")

# ---------------------------------------------------------------------

# here, else is not executed coz loop break nahi hua khtam hua hai as last iteration end ho chuki hai that's why else is not executed :

# program no. 1 : 

# for i in range(6):
#     print(i)
#     if i ==4:
#         break
# else: 
#     print("Sorry no i")

# program no. 2 : 

i = 0
while i<7:
    print(i)
    i=i+1
    # if i ==4:
    #     break
else:
    print("Sorry no i")
