import numpy as np

#these are functions that you can apply on numpy arrays
x = np.random.randint(0, 10, (10, 10))
np.all(x > 5, axis = 0) #checks for each column (because it moves down the row) and sees if everything is true, returns boolean array
np.any(x > 5, axis = 0) #checks for each column (because it moves down the row) and sees if one thing is true, returns boolean array
np.argsort(x) #returns the indexes as a list such that when you select them in this order, you yield a sorted array
np.apply_along_axis(sorted, axis = 0, arr = x) #applies a function to a specific axis. Returns result
np.argmin(x)
np.argmax(x)
np.min(x)
np.max(x, axis = 0) #you can use the axis argument in the above functions too

a, b = np.nonzero(x) #returns a tuple of numbers corresponding to a position in an array of non-zero value. Commonly used to find when something is true

x.min() #you can also use the builtin functions in the array object
x.max()
x.sum()
x.cumsum(axis = 0) #sums up along the rows in a cumulative fashion

np.unique(x, return_counts = False) #get unique items (remove duplicates). Return counts will give you a second value that gives you the counts of each unique item

#add more if needed