# Key Points -> Clear the Clutter 

# Write a program to clear the clutter inside a folder on your computer. You
# should use os module to rename all the png images from 1.png all the
# way till n.png where n is the number of png files in that folder. Do the
# same for other file formats. For example: sfdsf.png -- > 1.png vfsf.png -- >
# 2.png this.png -- > 3.png design.png -- > 4.png name.png -- > 5.png

# -----------------------------------------------------------------------------------

# Files for this -> clutteredFolder + file.txt and there is the pngs with one exception means another format like pdf etc

import os
from pathlib import Path

# for renaming :
# base_dir = Path(__file__).resolve().parent
# source = base_dir / "clutteredFolder" / "file.txt"
# destination = base_dir / "clutteredFolder" / "6.txt"
# os.rename(source, destination)  # rename the file
# or os.rename("clutteredFolder/file.txt, "clutteredFolder/6.tx")

folder = os.path.join(os.path.dirname(__file__), "clutteredFolder")
files = os.listdir(folder)
i=1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.png")
        i = i+1