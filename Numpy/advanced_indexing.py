import numpy as np
# everything here is also true for pytorch with slightly different names

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print(arr[2]) #prints third row
print(arr[:, 2]) #prints third column

y = arr.copy()
# sets 1 and 2 to 0
y[y < 3] = 0 # implicitly: y < 3 yields a mask of the same shape. You can feed a mask of the same shape in as an index
print(y)
y = arr.copy()
print(y[np.array([1,1,2])]) # you can repeat-index if needed
print(y[np.array([1,1,2]), 2]) # you can repeat-index if needed

# in this case: grabbing indices across a batch
take_list = np.array([1,2]) #common goal: iterate along one index, gather another index
print(np.take(y, take_list, axis = 1)) #gets index 1 and 2 on the rows
y[:, take_list] #equivalent to this

# in this case: grabbing indices that vary in a batch
take_list = np.array([1,1,2]) # assuming that we have B indices
expanded_take_list = np.expand_dims(take_list, axis = 1) # we need to cast it into B X 1
print(np.take_along_axis(y, expanded_take_list, axis = 1)) #in pytorch, equivalent function is torch.gather() 

