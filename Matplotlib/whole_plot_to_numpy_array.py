import numpy as np
import matplotlib.pyplot as plt

my_dpi = 100
# plt.figure()

fig, ax = plt.subplots(figsize=(800/my_dpi, 800/my_dpi), dpi=my_dpi) #this gives you an 800 x 800 arrya at the end

ax.plot([1,2,3])

#Image from plot
ax.axis('off')
fig.tight_layout(pad=0)

# To remove the huge white borders
ax.margins(0)

fig.canvas.draw()
image_from_plot = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
image_from_plot = image_from_plot.reshape(fig.canvas.get_width_height()[::-1] + (3,))
# this gives you a numpy array that contains he plot elements