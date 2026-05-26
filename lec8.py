# Key Points -> User Input

# ----------------------------------------------------------------


# using input() function
# it basically takes input in the form of string by default

a = input() # input in string
print("My name is", a) # print it

# ----------------------------------------------------------------

b = input("Enter Your Name : ")
print("Hey, My name is ", b)

# ----------------------------------------------------------------

num1 = input("Enter 1st No. - ")
num2 = input("Enter 2nd No. - ")
print("The Sum of ", num1, " and ", num2, " is ", num1+num2) # Give wrong output 12100 as by default it is string and it add them that is 12100, for calculation we have to typecast
# it is known as concatenation of two numbers

# ----------------------------------------------------------------

num3 = int(input("Enter 1st No. - "))
num4 = int(input("Enter 2nd No. - "))
print("Sum is ", num3+num4)
# there is actually calculation

# 2nd Method

num5 = input("Enter 1st No. - ")
num6 = input("Enter 2nd No. - ")
print(int(num5)+int(num6))

# ----------------------------------------------------------------

num6 = input("Enter 1st No. - ")
num7 = input("Enter 2nd No. - ") # if enter string on the place of nos then gives error, as we do 14+"Deepak" => Error
print(int(num6)+int(num7))