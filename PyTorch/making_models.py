import torch
from torch import nn

input = torch.zeros(size = (1, 28 * 28))

#this is an exmaple of a sequenential model.
stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )
stack(input) #this is how you call the sequential model

# this is an example of a whole, class-based model
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
