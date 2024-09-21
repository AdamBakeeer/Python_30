import numpy as np

#creating arrays
a = np.array([1,2,3])
print(a)
#2d arrays
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)
#3d arrays
c = np.array([[[1,2,3],[1,2,3]],[[2,3,4],[4,5,6]]])
print(c)

#checking number of dimensions
print(a.ndim)
print(b.ndim)
print(c.ndim)

#defining number of dimensions
d = np.array([1,12,2,3,4], ndmin=5)
print(d)
print(d.ndim)


