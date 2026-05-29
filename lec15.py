# Key Points -> For Loop : 

# -----------------------------------------------------------------

# 1st Program

# name = "Deepak"
# for i in name:
#     print(i)
#     if(i=="p"):
#         print("This is Something special")


# 2nd Program

# colors = ['Red', 'Green', 'Pink', 'Yellow', 'White', 'Black']
# for color in colors:
#     print(color) # color i variable use in for loop
#     for i in color: # nested for loop
#         print(i)

# -----------------------------------------------------------------

# range() : use in for loop as range from where to where you need to print : 

for k in range(10):
    print(k+1)
    # print(k)
    # print(k+2)

for i in range(1,9): # means 1 to 9 not print 9 it's only upto 8 only
    print(i)

for i in range(0, 11, 2):
    print(i)