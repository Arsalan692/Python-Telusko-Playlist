import numpy as np

# Shape of an array
# array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(array.shape)

# Reshaping arrays
# array2 = np.array([20, 20, 20, 21, 21, 21, 22, 22, 22])
# array3 = np.array([45, 87, 64, 82, 45, 87, 64, 69, 42])
# re_ar1 = array2.reshape(3, 3)
# re_ar2 = array3.reshape(3, 3)
# for i in range(3):
#     print(f"{re_ar1[i]} --> {re_ar2[i]}")

# Reshaping into three dimensional array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(array.reshape(2, 2, 2))






