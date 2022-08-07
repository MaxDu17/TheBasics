import torch
from torch import nn

input = torch.zeros(size = (1, 28 * 28))

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
