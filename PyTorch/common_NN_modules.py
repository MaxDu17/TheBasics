from torch import nn

nn.MaxPool2d(kernel_size = 2, return_indices = False) #pools a 2x2 area.
nn.MaxUnpool2d(kernel_size = 2) #takes in indices, which are created above if needed

# activation functions
nn.Softmax()
nn.Tanh()
nn.ReLU()
nn.LeakyReLU()

