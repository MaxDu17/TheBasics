import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor

#### this is how you use an existing dataset
training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor() #what to apply to the images
) #returns a Dataset class

img, label = training_data[1] #supports indexing

# how to creat a custom dataset
class CustomImageDataset(Dataset):
    def __init__(self):
        pass

    def __len__(self):
        pass

    def __getitem__(self, idx):
        pass

