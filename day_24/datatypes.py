import numpy as np

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

a = np.array([1, 2, 3, 4])
print(a.dtype)

b = np.array(['apple', 'banana', 'cherry'])
print(b.dtype)

#creating array with defined data type
c = np.array([1,2,3,4], dtype='S')
print(c)
print(c.dtype)

#CHANGING DATA TYPE USING ASTYPE
d = np.array([1.1,2.2,3.3])
newD = d.astype('i')
print(d)
print(newD)
print(newD.dtype)

e = np.array([1, 0, 3])

newE = e.astype(bool)

print(e)
print(newE)
print(newE.dtype)
