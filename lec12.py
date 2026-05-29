# Key Points -> If-Else conditional statements : 

# ------------------------------------------------------------

# there is -> if, if-else, if-else-elif, nested if-else-elif

# ------------------------------------------------------------

# Conditional Operators are -> (>, <, >=, <=, ==, !=)

# ------------------------------------------------------------

# 1st Program of if-else : 

# a = int(input("Enter Your Age: "))
# print("Your entered age is: ", a)
# if(a>18):
#     print("You can drive")
# else:
#     print("You cannot drive")
# print("Completed Executed") # it is always executed as it is not follow indentation and it is out of if-else condition

# 2nd Program of if-else : 

# applePrice = 210
# budget = 200
# if(applePrice<=budget):
#     print("Alexa, add 1 kg apples to the cart.")
# else:
#     print("Alexa, do not add apples to the cart.")

# ------------------------------------------------------------

# 1st program of if-elif-else

# num = int(input("Enter No. : "))
# if(num<0):
#     print(num, " is Smaller than 0")
# elif(num >0):
#     print(num, " is Greater than 0")
# else:
#     print(num, " is equals to 0")

# 2nd Program of if-else-elif (Many Conditions) : 

# num = int(input("Enter Number: "))
# if(num<0):
#     print("Number is Smaller than 0")
# elif(num==10):
#     print("Number is equals to 10")
# elif(num ==20):
#     print("Number is equals to 20")
# elif(num==50):
#     print("Number is equals to 50")
# else:
#     print("Number is Equals to 0 or Greather than 0")
# print("Happy Execution")

# ------------------------------------------------------------

# 3rd Program of Nested if-else-elif conditional statement : 

num = int(input("Enter No. : "))
if(num<0):
    print("Number is Negative")
elif(num>0):
    if(num<=10):
        print("Number is b/w 1 - 10")
    elif(num>10 and num<=20):
        print("Number is b/w 11 - 20")
    else:
        print("Number is Greater than 20")
else:
    print("Number is equals to 0")
    
