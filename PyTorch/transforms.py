import torch
from torchvision import transforms
# see this for more documentation https://pytorch.org/vision/stable/transforms.html#torchvision.transforms.Compose

#most transformations accept tensor and PIL images. They accept batches of tensor images, with the batch as the first dimension
#format is ([B], C, H, W)

#to compose transformations, use torch.nn.Sequential() or the

image =  torch.ones(size = (3, 255, 255))

transform = transforms.CenterCrop((100, 100))
transform = transforms.ColorJitter() #brightness, contrast, saturation, hue
transform = transforms.FiveCrop((100, 100)) #four corners and cneter crop. Returns tuple of images
transform = transforms.Grayscale()
transform = transforms.Pad(padding = 20, fill = (255, 255, 255)) #padding the image with a fill value
transform = transforms.RandomAffine(degrees = 20) #additionally ou can translate, scale, and shear
transform = transforms.RandomApply((transforms.ColorJitter(), transforms.Grayscale()), p = 0.3) #add a list of transformations here, will apply this whole list at random
transform = transforms.RandomCrop(size = (20, 20))
transform = transforms.RandomGrayscale(p = 0.1) #randomly converts to grayscale
transform = transforms.RandomHorizontalFlip(p = 0.5)
transform = transforms.RandomPerspective() #applies a random perspective transformation. Distortion_scale, p
transform = transforms.RandomResizedCrop(size = (100, 100)) #scale, ratio. Random crop that is resized to a desired size
transform = transforms.RandomRotation(degrees = 20)
transform = transforms.RandomVerticalFlip(p = 0.5)
transform = transforms.Resize(size = (100, 100))
transform = transforms.GaussianBlur(kernel_size = 3)
transform = transforms.RandomInvert(p = 0.2) #randomly invert the colors
transform = transforms.RandomPosterize(bits = 5, p = 0.5)
transform = transforms.RandomSolarize(threshold = 128, p = 0.5)
transform = transforms.RandomAdjustSharpness(sharpness_factor = 1.2, p = 0.5)
transform = transforms.RandomAutocontrast(p = 0.5)
transform = transforms.RandomEqualize(p = 0.5)
# transform = transforms.LinaerTransformation(transformation_matrix, mean_vector) #custom linear transformation, only for tensors
transform = transforms.Normalize(mean = (30, 30, 30), std = (1, 1, 1))
transform = transforms.RandomErasing() #randomly erase a rectangle
transform = transforms.ConvertImageDtype(dtype = torch.float32)
transform = transforms.ToPILImage()
transform = transforms.ToTensor()
transform = transforms.PILToTensor()
# transform = transforms.Lambda(lambda_here) #for generic lambda function
aug = transform(image)