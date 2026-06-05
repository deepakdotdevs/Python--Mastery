# Key Points : Exercise 2 : 

# ---------------------------------------------------------------------

import time

current_time = int(time.strftime('%H'))
current_time = int(input("Enter hour : "))
if(current_time>0 and current_time<12):
    print("Good Morning !!")
elif(current_time>=12 and current_time<17):
    print("Good Afternoon !!")
elif(current_time>=12 and current_time<0):
    print("Good Evening !!")