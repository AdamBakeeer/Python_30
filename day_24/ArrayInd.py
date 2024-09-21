import numpy as np

a = np.array([1,2,3,4,5])
print(a[0])

#accessing 2d arrays
b = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(b[0, 1])

#accessing 3d arrats
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(c[0, 1, 2])

#negative indexing
d = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', d[1, -1])