import torch
from torchvision import transforms
import random
# see this for more documentation https://pytorch.org/vision/stable/transforms.html#torchvision.transforms.Compose

#most transformations accept tensor and PIL images. They accept batches of tensor images, with the batch as the first dimension
#format is ([B], C, H, W)

image =  torch.ones(size = (3, 256, 256), dtype = torch.uint8) # our "image"

#cropping and padding
transform = transforms.CenterCrop((100, 100))
transform = transforms.RandomCrop(size = (20, 20))
transform = transforms.FiveCrop((100, 100)) #four corners and cneter crop. Returns tuple of images
transform = transforms.Pad(padding = 20, fill = (255, 255, 255)) #padding the image with a fill value
transform = transforms.RandomResizedCrop(size = (100, 100)) #scale, ratio. Random crop that is resized to a desired size

#linear  transformations
transform = transforms.RandomHorizontalFlip(p = 0.5)
transform = transforms.RandomAffine(degrees = 20) #additionally ou can translate, scale, and shear
transform = transforms.RandomPerspective() #applies a random perspective transformation. Distortion_scale
transform = transforms.Resize(size = (100, 100))
transform = transforms.RandomRotation(degrees = 20)
transform = transforms.RandomVerticalFlip(p = 0.5)
# transform = transforms.LinearTransformation(transformation_matrix, mean_vector) #custom linear transformation, only for tensors

# colors and other visual properties
transform = transforms.ColorJitter() #brightness, contrast, saturation, hue
transform = transforms.Grayscale()
transform = transforms.RandomGrayscale(p = 0.1) #randomly converts to grayscale
transform = transforms.RandomInvert(p = 0.2) #randomly invert the colors
transform = transforms.RandomPosterize(bits = 5, p = 0.5)
transform = transforms.RandomSolarize(threshold = 128, p = 0.5)
transform = transforms.GaussianBlur(kernel_size = 3)
transform = transforms.RandomAdjustSharpness(sharpness_factor = 1.2, p = 0.5)
transform = transforms.RandomAutocontrast(p = 0.5)
transform = transforms.RandomEqualize(p = 0.5)

# misc and composed
transform = transforms.RandomApply((transforms.ColorJitter(), transforms.Grayscale()), p = 0.3) #add a list of transformations here, will apply this whole list at random
transform = transforms.RandomErasing() #randomly erase a rectangle
transform = transforms.Normalize(mean = (30, 30, 30), std = (1, 1, 1))
# transform = transforms.Lambda(lambda_here) #for generic lambda function

#housekeeping
transform = transforms.ConvertImageDtype(dtype = torch.float32)
transform = transforms.ToPILImage()
transform = transforms.ToTensor()
transform = transforms.PILToTensor()

# compose transform
transform = transforms.Compose([transforms.CenterCrop(10),transforms.PILToTensor()])

#automatic augmentation policies
transform = transforms.AutoAugment(transforms.autoaugment.AutoAugmentPolicy.IMAGENET) #CIFAR10, SVHN are also options
transform = transforms.RandAugment(num_ops = 2, magnitude = 9) #an out-of-the-box augmenter
transform = transforms.TrivialAugmentWide() #another out-of-the-box augmenter

image_out = transform(image)

###### functional transforms ######
# functional transforms have no random number generators; they are just transformation functions. You make your own function
class MyRotationTransform:
    def __init__(self, angles):
        self.angles = angles

    def __call__(self, x):
        angle = random.choice(self.angles)
        return transforms.functional.rotate(x, angle) #this is one type of functional

image_out = MyRotationTransform(angles=[-30, -15, 0, 15, 30])

#linear transformations
image_out = transforms.functional.affine(image, angle = 23, translate = (2, 3), scale = 1.3, shear = 30)
image_out = transforms.functional.crop(image, top = 20, left = 20, height = 100, width = 100)
image_out = transforms.functional.hflip(image)
image_out = transforms.functional.vflip(image)
image_out = transforms.functional.center_crop(image, output_size = (250, 250))
image_out = transforms.functional.perspective(image, startpoints = [(0, 0), (255, 0), (0, 255), (255, 255)], endpoints =
                                              [(0, 0), (120, 0), (0, 230), (255, 255)])
image_out = transforms.functional.rotate(image, angle = 23)

#cropping and padding
image_out = transforms.functional.pad(image, padding = 10)
image_out = transforms.functional.resize(image, size = (20, 25))
image_out = transforms.functional.resized_crop(image, top = 20, left = 20, height = 100, width = 100, size = (250, 250))
image_out = transforms.functional.five_crop(image, size = (200, 200)) #returns a tuple
image_out = transforms.functional.ten_crop(image, size = (20, 20))

# color and other visual properties
image_out = transforms.functional.adjust_brightness(image, brightness_factor = 1.5)
image_out = transforms.functional.adjust_contrast(image, contrast_factor = 1.5) #see documentation for how these numbers behave
image_out = transforms.functional.adjust_gamma(image, gamma = 1.2)
image_out = transforms.functional.adjust_hue(image, hue_factor = 0.1)
image_out = transforms.functional.adjust_saturation(image, saturation_factor = 1.5)
image_out = transforms.functional.adjust_sharpness(image, sharpness_factor = 1.5)
image_out = transforms.functional.autocontrast(image)
image_out = transforms.functional.gaussian_blur(image, kernel_size = 1)
# image_out = transforms.functional.equalize(image) #equalizes the historgram (only works with uint8 datatypes)
# image_out = transforms.functional.posterize(image, bits = 5) #only works on uint8
image_out = transforms.functional.invert(image)
image_out = transforms.functional.normalize(image.float(), mean = 10, std = 1) # normalizes each pixel
image_out = transforms.functional.solarize(image, threshold = 230)
image_out = transforms.functional.rgb_to_grayscale(image)
# image_out = transforms.functional.to_grayscale(image) #only works for PIL images

# misc and housekeeping
image_out = transforms.functional.convert_image_dtype(image, dtype = torch.float32)
data = transforms.functional.get_image_num_channels(image)
data = transforms.functional.get_image_size(image)
# image_out = transforms.pil_to_tensor(pil_image)
