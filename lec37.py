# Key Points : Secret Code Language : 

# ----------------------------------------------------------

# Write a python program to translate a message into secret code language. Use the rules below
# to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
# now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to
#   the beginning

# Your program should ask whether you want to code or decode

# ----------------------------------------------------------

# Program Code : 

msg = input("Enter Message: ")
choice = input("Enter 'c' for coding & 'd' for decoding: ")
if(choice=='c'): # means coding
    if(len(msg)<3):
        print(f"Coded Msg coz msg is less than 3: ", msg[::-1])
    else:
        coded = "abc"+msg[1:]+msg[0]+"xyz"
        print(f"CODED MESSAGE: {coded}")
elif(choice=='d'): 
    if(len(msg)<3):
        print(f"Decoded Message as Length is less than 3: ")
    else:
        temp = msg[3:-3]
        decoded = temp[-1]+temp[:-1]
        print(f"DECODED Message: {decoded}")
else:
    print("Invalid Choice")
    