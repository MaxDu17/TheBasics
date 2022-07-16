from torch import nn
import torch
import numpy as np

# you can abstract things away like this
def encoder_block(going_in, out):
    return nn.Sequential(
        nn.Conv2d(going_in, out, kernel_size=4, padding=1, stride=2),
        nn.BatchNorm2d(out),
        nn.LeakyReLU(negative_slope=0.2)
    )

# if you don't have any business in-between encoder  blocks, this is the easiest.
# (see U-network for an implementation that uses nn.ModuleList)
encoder = nn.Sequential(
        encoder_block(3, 64),
        encoder_block(64, 128),
        encoder_block(128, 256),
        encoder_block(256, 512),
        encoder_block(512, 512),
        encoder_block(512, 512),
        encoder_block(512, 512)
    )

image = torch.Tensor(np.ones((1, 3, 256, 256))) #an "image"
prediction = encoder(image)
print(prediction.shape) #512 x 2 x 2
