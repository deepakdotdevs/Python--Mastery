# Key Points -> Match case statement (Like switch case in Java or C++)

# -----------------------------------------------------------------

x = int(input("Enter the Value of x: "))
match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case 2:
        print("x is two")
    case _ if(x!=90):
        print(x, " is not equals to 90")
    case _ if(x!=80):
        print(x, " is not equals to 80")
    case _: # this is for the default case
        print("x is i don't know coz this is a else case")


    # break statement is not mandantory or neccessary
    # there we use if-else also as there we create multiple default cases