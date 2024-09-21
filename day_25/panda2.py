#panda series : pandas series like a column in a table 1d array holding any type of data
import pandas as pd
import numpy as np

a = [1, 7, 2]
myvar =pd.Series(a)
print(myvar)

#SERIES WITH A CUSTOM INDEX

nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1,2,3,4,5])
print(s)

#Creating Pandas Series from a Dictionary
dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
d = pd.Series(dct)
print(d)

#Creating a Pandas Series Using Linspace
e=pd.Series(np.linspace(5, 20, 10))
print(e)

