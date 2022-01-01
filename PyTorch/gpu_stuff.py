import torch
from torch import nn

device = 'cuda' if torch.cuda.is_available() else 'cpu' #this will determine which device
x = torch.tensor([1, 2])
x.to(device) #move tensor to device

#dummy model to demonstrate how to move a model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()

    def forward(self, x):
        return x

model = NeuralNetwork().to(device) #move the model itself to the gpu or the cpu
