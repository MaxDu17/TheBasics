from torch import nn

# linear function
nn.Linear(in_features = 20, out_features = 300) # for MLP

# activation functions
nn.Softmax()
nn.Sigmoid()
nn.Tanh()
nn.ReLU()
nn.LeakyReLU(negative_slope = 0.01)

# for images. These two functions undo each other
nn.Conv2d(in_channels = 3, out_channels = 8, kernel_size = 3, stride = 1, padding = 0)
nn.ConvTranspose2d(in_channels = 8, out_channels = 3, kernel_size = 3, stride = 1, padding = 0)

# image pooling
nn.MaxPool2d(kernel_size = 2, return_indices = False) #pools a 2x2 area.
nn.MaxUnpool2d(kernel_size = 2) #takes in indices, which are created above if needed

# batchnorm
nn.BatchNorm2d(num_features = 20) # num_features are the things we aren't normalizing across

# sequence modeling
nn.LSTM(input_size = 20, hidden_size = 20) # see LSTM model
nn.Transformer() # see Transformer
