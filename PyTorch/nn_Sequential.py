import torch
from torch import nn
import torch.nn.functional as F


input = torch.zeros(size = (1, 28 * 28))
#this is an exmaple of a sequential model.
# note how we don't have to keep track of the weights and baises anymore
stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

def init_weights(m):
    print(m)
    if type(m) == nn.Linear:
        m.weight.data.fill_(1.0)
        print(m.weight)

stack.apply(init_weights) #you can apply initializations this way

stack(input) #this is how you call the sequential model
