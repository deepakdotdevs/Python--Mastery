# Key Points -> Exercise 9 Shoutouts to Everyone 

# Write a program to pronounce list of names using win32 API. If you are given a list l as
# follows:

# l = ["Rahul", "Nishant", "Harry"]

# Your program should pronouce:

# Shoutout to Rahul
# Shoutout to Nishant
# Shoutout to Harry

# Note: If you are not using windows, try to figure out how to do the same thing using
# some other package

# -----------------------------------------------------------------------------

# Solution : 
# pip install pyttsx3

# import pyttsx3

# engine = pyttsx3.init()

# engine.say("One")
# engine.runAndWait()

# engine.say("Two")
# engine.runAndWait()

# engine.say("Three")
# engine.runAndWait()

import pyttsx3
import time

engine = pyttsx3.init("sapi5")

names = []

while True:
    name = input("Enter a name or 'quit' to quit: ")

    if name.lower() == "quit":
        break

    names.append(name)

for name in names:
    engine.say(f"Shoutout to {name}")
    engine.runAndWait()   
    time.sleep(0.5)        