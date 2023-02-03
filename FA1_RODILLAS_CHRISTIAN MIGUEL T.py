#!/usr/bin/env python
# coding: utf-8

# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a
# mile.

# In[1]:


km = input("How many kilometers?")
mi = 1.61
answer = float(km)/mi

print(km + "km is equal to " + "%.2f" %answer + "mi")


# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?

# In[3]:


import math
km = input("How many kilometers?")
miles = float(km) / 1.609344 
time = 256.2 
timemin = time / 60
timehr = timemin / 60

pacesec = (float(time)*float(km)) / float(miles)
pacemin = (float(timemin)*float(km)) / float(miles)
averagehr = float(miles) / (float(timehr)*float(km))


print("The average pace is " +str(round(pacesec,2)) + " seconds per mile")
print("The average pace is " + str(round(pacemin,2)) + " minutes per mile")
print("The average speed is " + str(round(averagehr,2)) + " miles per hour")


# In[ ]:




