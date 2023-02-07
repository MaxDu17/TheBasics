import imageio
import numpy as np
import tqdm
skip = 10
im = imageio.get_reader("data/Close Right 2.mp4")
counter = 0
im_list = list()
for k in im:
    if counter % skip == 0:
        im_list.append(k)
    counter += 1

master_image = np.zeros_like(im_list[0].astype(np.float64))
for i, frame in enumerate(im_list):
    opacity = 1 / len(im_list)
    master_image += opacity * frame.astype(np.float64)

imageio.imsave("trajectory.png", master_image)

