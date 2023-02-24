import torch
from torch import nn

input = torch.ones(size = (1, 28 * 28))

# a dummy model to train
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

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork()
loss_fn = nn.CrossEntropyLoss() #many more losses available, or you can do your own!
optimizer = torch.optim.Adam(model.parameters(), lr=2e-4, betas=(0.5,0.999))

#standard training procedure; this is a bogus objective but it shows how it works
pred = model(input)
y = torch.ones_like(pred) #just for show

# loss = torch.sum(pred) # any scalar function output can work
loss = loss_fn(pred, y)
# for gradient accumulation, do loss.backward() every time, and then optimizer.step() / optimizer.zero_grad() after a certain namount of time

####################### THE PART YOU CARE ABOUT #######################
optimizer.zero_grad() #gradients add up, so you must reset
loss.backward() #backpropagation. Put a vector into the backward() to compute the jacobian product
optimizer.step() #applies change
################################################################

#### ignoring part of the computation graph ###
w = torch.rand(size = (10, 20))
x = torch.rand(size = (1, 10))
b = torch.rand(size = (1, 20))
with torch.no_grad():
    z = x @ w + b
print(z.requires_grad) #does not propagate because we used a non-gradient environment
print(w.requires_grad) #if z is not tracked, its dependencies are also not tracked (because it's upstream)

#using detach() to do the same
z = torch.matmul(x, w)+b
z_det = z.detach() #detaching removes a variable from optimizing, which affects all upstream

