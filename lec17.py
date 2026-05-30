# Key Points -> break and continue in python & Do-while loop : Use in Loop

# -----------------------------------------------------------------

# break -> is used for exit from the loop at particular iteration
# Continue -> is used for skip a particular iteration and continue from that next 

# -----------------------------------------------------------------

# break Program : means exist from the loop

# for i in range(12):
#     if(i==10): # upto 5*10 gives output
#         break
#     print("5 ❌ ", i+1, " = ", 5*(i+1))
#     # if(i==10): # upto 5*11 gives output
#     #     break
# print("Exit from the loop not the part of loop/break/continue")

# ---------------------------------------------------------------------

# continue -> skip the iteration not exist from the loop : 

# for i in range(12):
#     if(i==10):
#         print("Skip the iteration")
#         continue
#     print("5 ❌ ", i, " = ", 5*i)

# ---------------------------------------------------------------------

# do while loop : 

i = 0
while True:
    print(i)
    i = i+1
    if(i%100 == 0): # condition is false
        break


while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number>0:
        break
