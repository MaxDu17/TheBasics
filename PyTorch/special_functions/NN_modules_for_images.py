from torch import nn

# for images. These two functions undo each other
nn.Conv2d(in_channels = 3, out_channels = 8, kernel_size = 3, stride = 1, padding = 0)
nn.ConvTranspose2d(in_channels = 8, out_channels = 3, kernel_size = 3, stride = 1, padding = 0)

# image pooling
nn.MaxPool2d(kernel_size = 2, return_indices = False) #pools a 2x2 area.
nn.MaxUnpool2d(kernel_size = 2) #takes in indices, which are created above if needed

# batchnorm
nn.BatchNorm2d(num_features = 20) # num_features are the things we aren't normalizing across. For Batch X H X W (CNNs)
nn.BatchNorm1d(num_features = 20) #for batch X D
