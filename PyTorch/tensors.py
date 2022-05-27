import numpy as np
import torch

#between numpy and torch. The key!
x_np = np.array([3., 4.])
x = torch.from_numpy(x_np)
x_np = x.numpy()

#device can be cpu or gpu (cuda)
x = torch.tensor([1., 2.], device = "cpu", dtype = torch.float32, requires_grad = True) #like numpy, you can make tensors from lists
#requries grad is true by default
x = torch.ones_like(x)
x = torch.rand_like(x) #random numbers between 0 and 1
x = torch.rand(size = (2, 3))
x = torch.ones(size = (2, 3))
x = torch.zeros(size = (2, 3))

print(x.shape)
print(x.dtype)
print(x.device)

# casting
x_casted = x.double() #.float(), .int()
x_casted = x.type(torch.FloatTensor) #DoubleTensor, IntTensor

#other common operations
x.squeeze() #remove extra dimension
x = torch.unsqueeze(x, dim = 1) #add an extra dimension at axis 1
x = x.view(-1, 2) # [3, 2] but no explicit reshape
x = x.reshape(-1, 2) # explicit shaping (copies tensor)
x = torch.transpose(x, 0, 1) #flipping two axes
x = torch.ravel(x) #flatten

#scalars to python scalars
x = torch.ones((1, ))
print(x.item())

#numpy-identical slicing applies with tensors. We will not repeat it here

#join tensors
x = torch.zeros(size = (2, 3))
y = torch.zeros(size = (2, 3))
z = torch.zeros(size = (2, 3))
w = torch.cat([x, y, z], dim = 0) #concatenate along the first axis, which yields (6, 3)
print(w.shape)
w = torch.stack([x, y, z], dim = 0) #stacks (adds another dimension) to 3, 2, 3
print(w.shape)
w_list = torch.chunk(w, 3, dim = 0)
print(w_list[0].shape) # [1, 2, 3] because we split [3, 2, 3] into 3 chunks

x = torch.tensor([True, False, True])
x = ~x #you can invert booleans like this
print(x)

#all tensor operations use the same symbols as numpy
