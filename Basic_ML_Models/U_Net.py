import numpy as np
import torch
from torch import nn
from torch.nn import functional as F
import torchvision.models as models
import torchvision.transforms as transforms
from torchsummary import summary

class UNetwork(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.input_dim = tuple(input_dim)
        self.img_C, self.img_H, self.img_W = self.input_dim
        self.activations = []

        self.encoder = nn.ModuleList([
            self.encoder_block(self.img_C, 64, bn = False),
            self.encoder_block(64, 128),
            self.encoder_block(128, 256),
            self.encoder_block(256, 512),
            self.encoder_block(512, 512),
            self.encoder_block(512, 512),
            self.encoder_block(512, 512)
        ])

        self.decoder = nn.ModuleList([
            self.decoder_block(512, 512, dropout = True),
            self.decoder_block(1024, 512, dropout=True),
            self.decoder_block(1024, 512, dropout=True),
            self.decoder_block(1024, 256, dropout=False),
            self.decoder_block(512, 128, dropout=False),
            self.decoder_block(256, 64, dropout=False),
        ])

        self.out = nn.Sequential(
            nn.ConvTranspose2d(128, 3, kernel_size = 4, padding = 1, stride = 2),
            nn.Tanh()
        )

    def encoder_block(self, going_in, out, bn = True):
        if bn:
            return nn.Sequential(
                nn.Conv2d(going_in, out, kernel_size = 4, padding = 1, stride = 2),
                nn.BatchNorm2d(out),
                nn.LeakyReLU(negative_slope = 0.2)
            )
        else:
            return nn.Sequential(
                nn.Conv2d(going_in, out, kernel_size = 4, padding = 1, stride = 2),
                nn.LeakyReLU(negative_slope = 0.2)
            )

    def decoder_block(self, going_in, out, dropout = True):
        if dropout:
            return nn.Sequential(
                nn.ConvTranspose2d(going_in, out, kernel_size = 4, padding = 1, stride = 2),
                nn.BatchNorm2d(out),
                nn.Dropout2d(p = 0.5),
                nn.ReLU()
            )
        else:
            return nn.Sequential(
                nn.ConvTranspose2d(going_in, out, kernel_size=4, padding=1, stride=2),
                nn.Dropout2d(p=0.5),
                nn.ReLU()
            )

    def forward(self, images):
        self.activations.clear()
        x = images
        for module in self.encoder:
            x = module(x)
            self.activations.append(x)
        self.activations.pop()  # discard the last one because it's the embedding

        for module in self.decoder:
            x = module(x)
            x = torch.cat((x, self.activations.pop()), dim = 1)

        return self.out(x)

image = torch.Tensor(np.ones((1, 3, 256, 256))) #an "image"
u_network = UNetwork((3, 256, 256))
output = u_network(image)
print(output.shape) #3 x 256 x 256