import h5py
import numpy as np

d1 = np.random.random(size = (1000,20))
d2 = np.random.random(size = (1000,200))
d3 = np.random.random(size = (1000,200))

hf = h5py.File('samples/data.h5', 'w') #makes a new file
hf.create_dataset("dataset_1", data = d1)

# we can also create groups (sets) of data
g1 = hf.create_group("group1")
g1.create_dataset("dataset_2", data = d2)

g2 = hf.create_group("group2/subfolder") # organization
g2.create_dataset("dataset_3", data = d3)
hf.close()

# structure:
# dataset 1
# group1 / dataset 2
# group2 / subfolder / dataset 3


# reading
hf = h5py.File('samples/data.h5', 'r')
print(hf.keys())
d1 = hf["dataset_1"]
d1 = np.array(d1)
print(d1.shape)

d2 = hf["group1/dataset_2"]
d2 = np.array(d2)
print(d2.shape)

d3 = hf.get("group1/subfolder/dataset_3") #the .get() is more reliable
d3 = np.array(d3)
print(d2.shape)
hf.close()
