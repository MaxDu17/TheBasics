# https://scipy-lectures.org/packages/scikit-image/index.html
# there are a lot of image features to use, including image segmentation

import skimage
from skimage import data  # most functions are in subpackages
from skimage import filters # various filters to use in image processing
from skimage import io
from skimage import img_as_float
import numpy as np

# most scikit-image functions us np arrays, which is very helpful

camera = data.camera() #example image we will be using
camera_float = img_as_float(camera) #directly between -1 and 1



###### IMAGE PREPROCESSING #####
# you can do a lot of different filters
# https://scikit-image.org/docs/stable/api/skimage.filters.html
output = filters.sobel_h(camera) #local filter

from skimage import exposure
output = exposure.equalize_hist(camera)

val = filters.threshold_otsu(camera)
output = camera < val #segmentation mask


io.imsave("test.png", output)