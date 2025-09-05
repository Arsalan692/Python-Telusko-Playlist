
import numpy as np

# Operations that come handy in data analysis
one_dim = np.array([1, 2, 3, 4, 5, 6, 7,8,9])
two_dim = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Sum() function
# print(one_dim.sum())
# print(sum(two_dim))
# print(two_dim.sum())

# Max and Min
# print(one_dim.min())
# print(two_dim.max())

# Summing elements in rows and column respectively in two-dim array
# print(two_dim.sum(axis=0)) # This adds up the columns
print(two_dim.sum(axis=1))   # This adds up the rows




