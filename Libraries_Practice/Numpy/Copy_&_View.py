
import numpy as np

# Copy() Command
# array = np.array([1, 2, 3, 4, 5])
# array_copy = array.copy()
# array[0] = 69
# print(array_copy)

# View() command
array2 = np.array([1, 2, 3, 4, 5])
array2_view = array2.view()
array2[1] = 69
# print(array2_view)

# Python to recall weather it is a view or copy
print(array2_view.base)
print(array2.base)





