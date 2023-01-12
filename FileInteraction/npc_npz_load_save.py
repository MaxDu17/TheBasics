import numpy as np

arr_1 = np.ones((1, 100))
arr_2 = np.ones((100, 234))
arr_3 = np.ones((2, 3))

arr_dict = {"a" : arr_1, "b" : arr_2}
np.save("samples/simple_arr.npy", arr_1) #only numpy arrays
np.save("samples/complicated_arr.npy", arr_dict, allow_pickle = True) #this allows you to save intricate datastructures

np.savez("samples/arr_struct.npz", a = arr_1, b = arr_2, c = arr_3) #use keyword arguments to name the file

# for compressed files
# np.savez_compressed("samples/arr_struct.npz", a = arr_1, b = arr_2, c = arr_3) #use keyword arguments to name the file

#### loading ###
x = np.load("samples/simple_arr.npy")
print(x.shape) #should be single array
y = np.load("samples/complicated_arr.npy", allow_pickle = True)
print(y[()].keys()) #you need this special trick to access

z = np.load("samples/arr_struct.npz")
print(z.files)
print(z["a"].shape)
