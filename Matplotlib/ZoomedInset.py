import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset

plt.rcParams["lines.linewidth"] = 3

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
line, line2 = ax.plot(t, s, t, s + 0.3)

axins = ax.inset_axes([0.2, 0.2, 0.2, 0.2]) #x, y, width, height
axins.plot(t, s, t, s + 0.3) #you're basically replotting

# sub region of the original image
x1, x2, y1, y2 = -0.2, 0.2, 1.4, 1.5
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
axins.set_xticklabels([])
axins.set_yticklabels([])


ax.indicate_inset_zoom(axins, edgecolor="black")
plt.show()