import numpy as np #here we use a numpy array as a nonprimitive type

def modify(x):
    x = x + 1 #make a local copy; doesn't change

def modify_in_place(x):
    x += 1

def modify_in_place_list(x):
    x[0] = 14
    # x += 1 #these are in place operations
    # they affect any non-primitives

# primitive types are not affected
y = 2
modify_in_place(y)
print(y) #does not change!

# but complicated types (rule of thumb: lists, numpy arrays, tensors) are passed by reference
y = np.array([1, 2, 3])
print(y)
modify_in_place_list(y)
print(y) #does change!

y = [1, 2, 3]
print(y)
modify_in_place_list(y)
print(y) #does change!

z = np.array([6, 7, 8])
z = y # now they are referencing the same thing
z[0] = 100
print(y)
print(z)

y = np.array([1, 2, 3])
z = np.array([6, 7, 8])
z = y.copy()
z[0] = 100
print(y)
print(z)
