from torch import nn

# linear function
nn.Linear(in_features = 20, out_features = 300) # for MLP

# activation functions
nn.Softmax()
nn.Sigmoid()
nn.Tanh()
nn.ReLU()
nn.LeakyReLU(negative_slope = 0.01)


