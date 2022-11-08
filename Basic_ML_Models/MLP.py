from torch import nn
import torch
import numpy as np
import matplotlib.pyplot as plt

in_dim = 2
out_dim = 1
hidden_dim = 10
mlp = nn.Sequential(
    nn.Linear(in_dim, hidden_dim),
    nn.ReLU(),
    nn.Linear(hidden_dim, hidden_dim),
    nn.ReLU(),
    nn.Linear(hidden_dim, out_dim),
)

# testing the model
# x = torch.ones((in_dim,))
# y = mlp(x)


###  FOR A SIMPLE DEMO OF LINEAR REGRESSION ###
pos_examples = torch.randn((100, 2)) + 3
neg_examples = torch.randn((100, 2)) - 3
training = torch.cat((pos_examples, neg_examples))
labels = torch.ones((training.shape[0], 1))
labels[100 : ] = 0


fig, ax = plt.subplots()
pos = pos_examples.numpy()
x_data_pos = pos[:, 0]
y_data_pos = pos[:, 1]
ax.scatter(x_data_pos, y_data_pos, color = "green")

neg = neg_examples.numpy()
x_data_neg = neg[:, 0]
y_data_neg = neg[:, 1]
ax.scatter(x_data_neg, y_data_neg, color = "red")
plt.show()

loss_fn = nn.BCEWithLogitsLoss()  # many more losses available, or you can do your own!
optimizer = torch.optim.Adam(mlp.parameters(), lr=2e-4, betas=(0.5,0.999))

for i in range(1000):
    prediction = mlp(training)
    loss = loss_fn(prediction, labels)
    if i % 100 == 0:
        print("Loss: ", loss.item())
    optimizer.zero_grad()  # gradients add up, so you must reset
    loss.backward()  # backpropagation. Put a vector into the backward() to compute the jacobian product
    optimizer.step()  # applies change


# this is how to do a grid plot
x_min, x_max = training[:, 0].min() - 1, training[:, 0].max() + 1
y_min, y_max = training[:, 1].min() - 1, training[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))


Z = torch.nn.functional.sigmoid(mlp(torch.tensor(np.c_[xx.ravel(), yy.ravel()], dtype = torch.float32))).detach().numpy()

# Put the result into a color plot
Z = Z.reshape(xx.shape)

fig, ax = plt.subplots()
ax.contourf(xx, yy, Z, levels = 100,  cmap = "RdYlGn") #, cmap=plt.cm.Paired)
ax.scatter(x_data_pos, y_data_pos, color = "cyan")
ax.scatter(x_data_neg, y_data_neg, color = "pink")

plt.show()

