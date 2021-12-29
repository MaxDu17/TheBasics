import numpy as np

#### copying ####
arr = np.array([1, 2, 3, 4, 5])
b = arr #this DOES NOT copy
c = arr.copy()  #this does copy

#block matrices
a = np.ones([2, 2])
b = np.ones([2, 2])
arr = np.block([a, b])
arr = np.vstack([a, b]) #vertical stacking. Stacking increases the dimension
arr = np.hstack([a, b])
arr = np.tile(a, (2, 2)) #tiles it in a 2 x 2 pattern, yielding a 4 x 4 array

arr = np.concatenate((a, b), axis = 0) #concatenating rowwise. It generalizes hstack and vstack to higher dimensions
print(arr.shape)