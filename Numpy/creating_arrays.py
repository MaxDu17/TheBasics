import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize) #prevents array truncation

arr = np.array([1, 2, 3, 4, 5], dtype = np.float32) #one way of making an array
#uint32, int8, float32 are the classics

#### key properties of arrays ####
print(arr.shape)
print(arr.dtype)
print(type(arr)) #this prints numpy array
print(arr.size) #total number of elements
print(arr.itemsize) #number of bytes per element

##########

arr = np.arange(10) #start from 0, write ints until you reach 10 exclusive
arr = np.arange(2, 10, dtype = float) #start from 2, end at 10 exclusive
arr = np.arange(2, 10, 0.1) #start from 2 and end at 10 exclusive with hops of 0.1
#arange can be numerically unstable and include the end value at times

arr = np.linspace(1, 4, 6) #make an array of 6 numbers that include 1 and 4

## now, some standard stuff ##
arr = np.zeros((2, 3, 2)) #shape tuple
arr = np.ones(2) #tuple implied

arr = np.random.random((2, 3))
arr = np.random.randint(10, 20, (2, 3))

x = np.zeros_like(arr) #mimic the shape
x = np.ones_like(arr)

arr = np.eye(3) #3 x 3 identity matrix
arr = np.eye(3, 6) #non-square identity

arr = np.diag([1, 2, 3, 4, 5]) #makes square array with this on the diagonal
diag_vals = np.diag(arr) #when fed with a 2d array, it extracts the diagonals

arr = np.vander([1, 2, 3, 4, 5]) #vandermonde matrix. columns are the provided vector raised to the nth power, decreasing from left to righ


arr = np.indices((3, 3))
#this returns a set of arrays that can be used as indices. If you had a matrix defined as M_ij = 2i + 3j, then you can
#just set M = 2* arr[0] + 3 * arr[1]. The key is the each element of arr varies in only one direction
x, y = np.meshgrid(np.arange(10), np.arange(10)) #this does the same thing but with lists instead of integers, so you have more freedom

arr = np.loadtxt("demo.csv", delimiter = ",", skiprows = 1)

