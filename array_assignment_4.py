#QUESTION
#Write a code to find maximum value from an array without using in-built function

from numpy import *
arr = array([123, 546, 789, 1234, 21, 56])
k = 0
for i in arr:
    if i >= k:
        k = i
print(k)







