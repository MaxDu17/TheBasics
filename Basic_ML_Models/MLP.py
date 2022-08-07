from torch import nn
import torch
import numpy as np

in_dim = 20
out_dim = 10
hidden_dim = 100
mlp = nn.Sequential(
    nn.Linear(in_dim, hidden_dim),
    nn.Linear(hidden_dim, hidden_dim),
    nn.Linear(hidden_dim, out_dim)
)

# testing the model
x = torch.ones((in_dim,))
y = mlp(x)
