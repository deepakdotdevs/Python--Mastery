# Key Point -> If-else-elif exercise problem : 

# ------------------------------------------------------------

# Time Module : 

# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

# ------------------------------------------------------------

import time

current_time = int(time.strftime('%H'))
if(current_time<12):
    print("Good Morning Guys!!!")
elif(current_time<17):
    print("Good Afternoon!!")
else:
    print("Good Evening!")
    