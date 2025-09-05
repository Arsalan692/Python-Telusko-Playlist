import numpy as np

one_dim = np.array([1, 2, 3])
two_dim = np.array([[1, 2, 3], [4, 5, 6]])

# Printing each element in two_dimensional array
# for i in two_dim:
#     for num in i:
#         print(num)

# Using .nditer command
# Handy way to print each element in any dimension
# for i in np.nditer(two_dim):
#     print(i)

# Figuring out the indexes --> Using ndenumerate
for index, element in np.ndenumerate(two_dim):
    print(index, element)





