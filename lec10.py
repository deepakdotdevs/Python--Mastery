# Key Points -> String Slicing and Operations on String

# ------------------------------------------------------

# Slicing : Square brackets for the slicing
names = "Deepak, Sahdev" # and i want only starting 6 characters of the whole string given
print(names[0:5]) # means 0 to 4 index means out is Deepa, including 0 but not 5
print(names[0:6]) # n+1 to print Deepak
print(len(names)) # to print the length of the string

fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word")

print(fruit[:6]) # python automatically adds 0
print(fruit[1:4])
print(fruit[2:])
print(fruit[:]) # here python automatically adds length of string

# Negative Slicing :
print(fruit[0:-3]) # count from backward side
print(fruit[-3:len(fruit)-1]) #  2:4
print(fruit[-3:-1]) # python use len(fruit) automatically

# Loop through a String : 
str_Line = "My Name is Deepak"
for characters in str_Line:
    print(characters)

# Quick Quiz : 
nm = "Harry"
print(nm[-4:-2]) # Output is ar
