import torch
from torch import nn
import torch.nn.functional as F

input = torch.zeros(size = (1, 28 * 28))

# this is an example of doing functional form
w = torch.ones(size = (12, 28 * 28))
b = torch.zeros(size = (12,))
x = F.linear(input, weight = w, bias = b) #Wx + B

#this is an exmaple of a sequenential model.
# note how we don't have to keep track of the weights and baises anymore
stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )
stack(input) #this is how you call the sequential model

# this is an example of an iterated module list
stack = nn.ModuleList((
    nn.Linear(28 * 28, 512),
    nn.ReLU(),
    nn.Linear(512, 512),
    nn.ReLU(),
    nn.Linear(512, 10),
    ))

y = input
for module in stack:
    y = module(y) #useful if you want to do modifications within the layers

# this is an example of a class-based model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()

    def forward(self, x):
        return x

model = NeuralNetwork()
model(input) #this is how you run a model (do not call forward() directly)

#how to iterate through parameters
for name, param in model.named_parameters():
    print(name)

for param in model.parameters():
    print(param)
