import numpy as np

x= np.array([[1, 2, 3], [4, 5, 6]])

# modifying the shape and stuff
w = x.reshape((6,)) #this gives a 1d array. Very tricky!
w = x.reshape((6, 1)) #this gives a 2d array
w = x.T #transposes the matrix
w = np.expand_dims(x, axis = 0) #the axis is the axis that will have the new dimension on it
w = x.flatten() #flattens the matrix
w = x.ravel() #this flattens but it is a copy (like a "view" in pytorch)

# rigid translations
# mat_new = np.array([[1, 2, 3], [4, 5, 6]])
# k is number of times you rotate
# grab the axis 0 and rotate towards axis 1. So this is CCW
w = np.rot90(x , k = 2, axes = (0, 1))
w = np.fliplr(x) #flip along axis 0
w = np.flipud(x) # flip along axis 1

# padding
# can have a tuple for padding
w = np.pad(x, pad_width = (1), mode = 'constant')

# sorting and other counting
w = np.argsort(x, axis = 1)
w = np.flatnonzero(x) # flattened indices that are non-zero
w = np.nonzero(x) #non-flattened indices that are non-zero
