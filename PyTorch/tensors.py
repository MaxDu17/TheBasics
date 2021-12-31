import numpy as np
import torch

#between numpy and torch
x_np = np.array([3., 4.])
x = torch.from_numpy(x_np)
x_np = x.numpy()

#device can be cpu or gpu (cuda)
x = torch.tensor([1., 2.], device = "cpu", dtype = torch.float32) #like numpy, you can make tensors from lists
x = torch.ones_like(x)
x = torch.rand_like(x) #random numbers between 0 and 1
x = torch.rand(size = (2, 3))
x = torch.ones(size = (2, 3))
x = torch.zeros(size = (2, 3))

print(x.shape)
print(x.dtype)
print(x.device)

#other native operations
print(x.sum())

#scalars to python scalars
x = torch.ones((1, ))
print(x.item())

#numpy-identical slicing applies with tensors. We will not repeat it here

# x = x.to("cuda") #how you move to gpu

#join tensors
x = torch.zeros(size = (2, 3))
y = torch.zeros(size = (2, 3))
z = torch.zeros(size = (2, 3))
w = torch.cat([x, y, z], dim = 0) #concatenate along the first axis, which yields (6, 3)
print(w.shape)

#all tensor operations use the same symbols as numpy