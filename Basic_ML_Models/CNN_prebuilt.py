from torchvision import datasets, transforms as T
import numpy as np
import torchvision.models as models
import torch

# https://pytorch.org/vision/0.8/models.html find everything here
resnet18 = models.resnet18(pretrained=True)
# print(resnet18.layer4) #you can index like this
# print(resnet18.layer4[0]) # and even finer granularity

# if you use a pretrained model, then you must use a normalization
normalize = T.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])

image = torch.Tensor(np.ones((1, 3, 224, 224))) #an "image"
image = normalize(image)
prediction = resnet18(image)
