import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
import imageio
import numpy as np

#first, the cv2 method
# img = cv2.imread("samples/sample.png")
# cv2.imwrite("samples/sample_writtencv2.png", img)
# print(img.shape) #length, width, depth

#now the matplotlib method
img = mpimg.imread("samples/sample.png")
plt.imsave("samples/sample_writtenplt.png", img) #this is NOT a numpy array
print(img.shape)


#now the pillow method
img = Image.open("samples/sample.png")
img.save("samples/sample_writtenpillow.png")
#unlike the previous two, this is not a simple numpy array

#saving the best for last: the imageio is the most convenient and has super neat features
im = imageio.imread("samples/sample.png")
im = np.array(im) # to turn into numpy array
plt.imsave("samples/save_writtenimagio.png", im)
im = imageio.imread("<screen>")
plt.imsave("samples/imageio_screenshot.png", im)
im = imageio.imread("<clipboard>")
plt.imsave("samples/imageio_clipboard.png", im)
