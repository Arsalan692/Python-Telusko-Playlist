#QUESTION:
#Create an array with 5 values & delete the value at index no. 2 without using in-built function.

import array as a

arr = a.array("i", [2, 4, 9, 7, 5])
for i in arr:
    if i == arr[2]:
        arr.remove(i)

print(arr)





