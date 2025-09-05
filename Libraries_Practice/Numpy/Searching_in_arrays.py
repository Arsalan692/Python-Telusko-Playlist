
import numpy as np

array1 = np.array([1, 2, 3, 4, 4, 6, 8, 9, 9, 8])

# We can use regular operators like ==, < , > , <= , >=
# print(np.where(array1 == 8))
# print(np.where(array1 <= 5))
print(np.where(array1 % 2 == 0))







