# To know the how many folders files are in "data" we created 

import os
folders = os.listdir("data")

print(folders)  # print folders in a list

for folder in folders: # print folders one by one
    print(folder)
    print(os.listdir(f"data/{folder}")) # use to print files under folders, example turotial 10 have tutorial.md and one line, it print it out

print(os.getcwd()) # used to know in which directory we work ..!!
os.chdir("/Users") # to change directory 
print(os.getcwd())