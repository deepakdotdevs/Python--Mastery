# Key Points : Dictionery 

# ---------------------------------------------------------------------

# Dictionaries are ordered collection of data items. They store multiple items in a single
# variable. Dictionary items are key-value pairs that are separated by commas and
# enclosed within curly brackets {}.

# ---------------------------------------------------------------------

# dic = {"Deepak":"Human being", "Spoon":"Object", "Age":20, "isOkay":"Yeah"}
# print(dic["Deepak"]) # output is "Human being"

# ---------------------------------------------------------------------

# Employee id with name : 
 
# # Here, intergers are keys and strings are values
# dic = {
#     101:"Deepak",
#     102:"Sahdev",
#     103:"Sharma",
#     104:"Kushagra",
#     105:"Harshit Singh"
# }
# # to print values :
# print(dic[103]) # gives Sharma

# # ---------------------------------------------------------------------

# # to print all of the dictionery : 
# dic1 = {"name":"Deepak", "age":20, "eligible":True}
# print(dic1)

# # to print particular value :
# print(dic1["age"]) # when we want problem should through an error when the key is not exists

# print(dic1.get("age")) # when we want no error should through by the program when the key is not exists

# # to access all of the keys of dictonery : 
# print(dic1.keys())

# print(dic1.values()) # give all values of keys

# # using loop :
# for i in dic1.keys():
#     print(dic1[i])

# for key in dic1.keys():
#     print(f"The value corresponding to the key {key} is {dic1[key]}")


# ---------------------------------------------------------------------

info = {'name':'Deepak', 'age':20, 'eligible':True}
print(info.items()) # print all the items with key and value both of the pairs

for key, value in info.items():
    print(f"The value corresponding to the key {key} is  {value}")
    