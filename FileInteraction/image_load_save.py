import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
import imageio
import numpy as np
# from skimage import io
from skimage.transform import resize


#first, the cv2 method. This is a little archaic
# img = cv2.imread("samples/sample.png")
# cv2.imwrite("samples/sample_writtencv2.png", img)
# print(img.shape) #length, width, depth

# skimage isa good one for direct numpy conversion
# logo = io.imread('http://scikit-image.org/_static/img/logo.png') # directly to numpy
# io.imagesave("samples/sample.png", logo)

#now the matplotlib method
img = mpimg.imread("samples/sample.png")
plt.imsave("samples/sample_writtenplt.png", img) #this is NOT a numpy array
print(img.shape)

#now the pillow method
img = Image.open("samples/sample.png")
img.save("samples/sample_writtenpillow.png")

# imageio is pretty convenient
im = imageio.imread("samples/sample.png")
# im = resize(im, (512, 512))[:, :, :-1] #remove the alpha channel. #if you want to do any resizing
im = np.array(im) # to turn into numpy array
plt.imsave("samples/save_writtenimagio.png", im)
im = imageio.imread("<screen>")
plt.imsave("samples/imageio_screenshot.png", im)
im = imageio.imread("<clipboard>")
plt.imsave("samples/imageio_clipboard.png", im)
