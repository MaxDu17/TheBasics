import torch
import torch.nn.functional as F

input = torch.zeros(size = (1, 28 * 28))

# this is an example of doing functional form
# requires you to manually keep track of weights and biases 
w = torch.ones(size = (12, 28 * 28))
b = torch.zeros(size = (12,))
x = F.linear(input, weight = w, bias = b) #Wx + B
