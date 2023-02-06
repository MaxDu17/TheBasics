from torch import nn
import torch

x = torch.rand(size = (2, 3))
x = torch.ravel(x) #flatten
norm = torch.linalg.norm(x)

### BOOLEAN OPERATIONS ###
x = torch.tensor([True, False, True])
x = ~x #you can invert booleans like this

### BATCH MATRIX MULTIPLICATION ##
x = torch.rand(size = (10, 20, 3))
y = torch.rand(size = (10, 3, 40))
z = torch.bmm(x, y)
print(z.shape) #10, 20, 40
