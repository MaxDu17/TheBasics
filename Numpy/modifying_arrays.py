import numpy as np

x = np.random.randint(0, 10, (10, 10))

y = x.reshape((100,)) #this gives a 1d array. Very tricky!
z = x.reshape((100, 1)) #this gives a 2d array

w = x.T #transposes the matrix
w = np.flip(x, axis = 0) #flip the rows
w = np.expand_dims(x, axis = 0) #the axis is the axis that will have the new dimension on it
w = x.flatten() #flattens the matrix
w = x.ravel() #this flattens but it is a copy (like a "view" in pytorch)