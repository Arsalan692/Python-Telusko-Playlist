#QUESTION
#Write a code to add 2 arrays using forloop.

from numpy import *

arr1 = array([1,2,3,4,5])
arr2 = array([6,8,9,10,11])

j = 0
list1 = []
for i in arr1:
    arr1_num = i
    addition = arr1_num + arr2[j]
    j += 1
    list1.append(addition)
print(list1)
