# Key Points -> String Methods : String are immutable

# --------------------------------------------------------

a = "deepak"
# we can't change string on inplace, but we can change string in another form, means we can make a new copy of it
print(a.upper()) # for uppercase, it gives us a new string in which all characters are in upper case

b = "DEEPAK"
print(b.lower()) # for lowercase

# ---------------------------------------------------------

# rstrip() : removes any trailing characters

c = "Deepak!!!!!!!!!!!!!!"
print(c)
# i dont'w want ! sign when i print in this way we use rstrip() for removing trailing 
print(c.rstrip("!"))

# ----------------------------------------------------------

# replace() : replaces all occurences of a string with another string

d = "Sahdev Sharma"
# i want to replace Sahdev Sharma to Deepak, in this such cases we use replace()
print(d.replace("Sahdev Sharma", "Deepak Jangid"))

# ------------------------------------------------------------

# split() : splits the given string at the specidied instance and returns the separated strings as list items

e = "Deepak Shadev Sharma Kushagra Harshit Singh" # space is mandantory for split() method
print(e.split(" "))

# ------------------------------------------------------------

# Capitalized() : The capitalize() method turns only the first character of the string to uppercase and the rest other
# characters of the string are turned to lowercase. The string has no effect if the first character is
# already uppercase.

p = "deepak jangid"
q = "deepak JanGiD"
print(q.capitalize()) # 1st character into uppercase character
print(q.capitalize()) # automatically converts rest of the characters into lowercase

# ------------------------------------------------------------

# center() : aligns the string to the center as per the parameters given by the user

v = "Welcome to the Console!!!!"
print(len(v))
print(len(v.center(50))) # it gives output of 50 as 26 characters (space is added in starting)

# ------------------------------------------------------------

# count() : It tells us that how many times a word is in the given string
g = "deepak!!!deepak!!!!!!!!!!!deepak!!!!pankaj!deepak"
print(g.count("deepak")) # given 4 as output

# ------------------------------------------------------------

# endswith() : checks if the string ends with a given value. Give output is Boolean form
print(g.endswith("pak")) # True
print(g.endswith("!!!")) # False

# we can even also check for a value in-between the string by providing start and end index positions
u = "welcome to the console!!!"
print(u.endswith("to", 4, 10))

# ------------------------------------------------------------

# find() : method searches for the first occurence of the given value and returns the index where it is present.
# returning type is -1 for false and 1 for true

str1 = "He's name is Deepak. He is an honest man"
print(str1.find("is"))

# ------------------------------------------------------------

# index() : method searches for the first occurence of the given value and return the index where it is present. If given value is absent from the string then raise an exception
str2 = "He's name is Deepak. He is an honest man"
print(str2.index("is"))

# ------------------------------------------------------------

# isalnum() : true when only consists A-Z, a-z, 0-9 only
str3 = "WelcomeToMyVlog"
print(str3.isalnum())
str4= "Welcome ToMyVlog"
print(str4.isalnum())

# ------------------------------------------------------------

# isalpha() : true when only consists A-Z and a-z only
str5 = "Welcome00" # gives false
str6 = "welcome " # gives false
str7 = "weoldAOJ" # gives true
print(str5.isalpha())
print(str6.isalpha())
print(str7.isalpha())
 
# ------------------------------------------------------------

# islower() : true if all characters in the string are lower case

str8 = "qwertyuiop"
print(str8.islower())

# ------------------------------------------------------------

# isprintable() : true if all values within the given string are printable, if not then return false
str9 = "it's is a printable"
str10 = "return false\n"
print(str9.isprintable())
print(str10.isprintable())

# ------------------------------------------------------------

# isspace() : true only and only if the string contains white spaces otherwise false
str11 = "       " # using space 
str12 = "           " # using tab
print(str11.isspace())
print(str12.isspace())

# ------------------------------------------------------------

# istitle() : true only if the first letter of each word of the string is capitalized otherwise false

str13 = "My Name Is Deepak"
str14 = "My Name is Deepak"
print(str13.istitle())
print(str14.istitle())

# ------------------------------------------------------------

# isupper() like exactly the islower() 

# ------------------------------------------------------------

# startswith() : if the string starts with a given value then yes otherwise false

str15 = "My name is Deepak"
print(str15.startswith("My"))

# ------------------------------------------------------------

# swapecase() : converts lower case into upper case and upper case into lower case

str16 = "My name is DEEPAK"
print(str16.swapcase())

# ------------------------------------------------------------

# title() : capitalize each letter of the word within the string

str17 = "my name is deepak"
print(str17.title())

# ------------------------------------------------------------
