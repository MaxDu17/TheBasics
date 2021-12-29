import numpy as np

## 1d slicing
x = np.arange(10)
print(x[2])
print(x[-1])
print(x[:-2])
print(x[2:5:2])

#array indexing
print(x[np.array([1, 3, 3])]) #you can index with another array

#2d indexing
y = np.eye(3)
print(y[2][2]) #this works, but is inefficient
print(y[2, 2]) #better

#masking
a = np.random.randint(10, 20, (10, 10))
mask = a > 15 #rookie mistake: the size of mask is constant; it does not depend on how many elements satisfy the boolean condition
print(a[mask]) #prints everything that is greater than 15 in a list
#if the mask has a lower dimension than the array, the output slice will be more than one dimensional as the mask is broadcast
print(a[np.where( a > 15)]) #the same thing as above but shorter

# argpartition to get top-k
x = np.random.randint(10, 2000, 100)
top_ten= np.partition(x, -10)[-10:] #argpartition pivots the array around some pivot (-10)
#everything before the pivot will be smaller than the pivot and everything after will be larger. Therefore, the top-k will be the last 10
print(top_ten)
#there also exists an argpartition version that returns the indexes of the top-k, which can be useful s


# advanced tricks
x = np.arange(5)
y = x[:, np.newaxis] #expands dimensions, like np.expand_dims does
x = np.ones((3, 3, 3, 3, 3))
print(x[1,...,2, 0]) #we select the second of the first dimension, all of the second and third dimension, the third of the fourth dimension, and the first of the last dimension

# SOMETHING VERY TRICKY: tuples vs lists vs boolean indexing
x[[1, 1, 1]] #essentially prints x[1] three times
x[[True, True, True]] #selects all three of x's first dimension
x[(1, 1, 1)] #selects x[1][1][1]

#programatic slicing
x = np.ones((3, 3, 3, 3, 3))
selection = (1, 1, slice(0, 2), 1, 1)
out = x[selection] #same as (1, 1, 0:2, 1, 1)
selection = (1, Ellipsis, 1)
out = x[selection] #same as (1, ..., 1)

# setting through slicing
x = np.arange(5)
x[2 : 4] = 30 #assigns element 2 and 3 to the value 30
#note: respect the data type! Truncations can occur if the np array is of a different datatype
x[0 : 4] = np.zeros(4) #slice and set equal to array