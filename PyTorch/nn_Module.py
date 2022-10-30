import torch
from torch import nn

input = torch.zeros(size = (1, 28 * 28))

# this is an example of a class-based model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

        nn.parameter.Parameter(data = torch.zeros((10, 10)), requires_grad = True) #this is how you keep track of a parameter
        # torch tensors by default are not kept track of.

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits


model = NeuralNetwork()
model(input) #this is how you run a model (do not call forward() directly)

#how to iterate through parameters
for name, param in model.named_parameters():
    print(name)

for param in model.parameters():
    print(param)
