import torchvision
import torch

# load imagenet this way
# imagenet_data = torchvision.datasets.ImageNet('./')

# root is the base directory that you want to save things under
mnist = torchvision.datasets.MNIST(root = "./", train = True, download = True, transform = None)
data_loader = torch.utils.data.DataLoader(mnist,
                                          batch_size=4,
                                          shuffle=True,
                                          num_workers=0)