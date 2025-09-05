#QUESTION
#write a code to reverse an array without using in-built function.

from array import *

ar = array("i", [1, 3, 6, 8, 45, 5, 6 ,8])

x = range(1, len(ar)+1)

ar_reverse = array("i", [])
for i in x:
    y = f"-{i}"
    ar_reverse.append(ar[int(y)])

print(ar_reverse)







