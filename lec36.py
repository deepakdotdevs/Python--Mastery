# Key Points : Raising Customer errors in Python :

# ---------------------------------------------------------------------

# raise keyword is used : 

# ---------------------------------------------------------------------

# a = int(input("Enter any value b/w 5 and 9 : "))
# if(a<5 or a>9):
#     raise ValueError("Value should be b/w 5 and 9")

# and that's how we raise built-in errors in python using raise keyword in python

# ---------------------------------------------------------------------

# salary = int(input("Enter Your Salary: "))
# if not 2000<salary<5000:
#     raise ValueError("Not a valid salary")

# ---------------------------------------------------------------------

user_input = input("Enter number b/w 5 and 9 (or type 'Quite' to exit): ")
if user_input.lower() == "quite":
    print(f"You type {user_input}. So you are quite")
else:
    try:
        num = int(user_input)
        if 5>num or 9<num:
            raise ValueError("Value should be b/w 5 and 9")
        else:
            print(f"You entered {num}")
    except Exception as e:
        print("Error: ", e)
