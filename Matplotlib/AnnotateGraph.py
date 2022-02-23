import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

ax = plt.subplot()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)
ax.set_ylim(-2, 2)
ax.axhline(y=0.5, color='r', linestyle='--') #horizontal line
ax.axvline(x=0.5, color='r', linestyle='--') #vertical line
#here we exercise all different sorts of annotation powers

ax.text(3, 1.5, r"$\sigma \sum_{x = 0}^\infty f(x)$  test")

# Create a Rectangle patch
rect = patches.Rectangle((0, 0), 1, 1, linewidth=1, edgecolor='r', facecolor='red')
ax.add_patch(rect)


ax.annotate('test', xy=(2, 1), xytext=(2, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )
ax.grid() #use plt.grid() if the grids don't show up
ax.legend([line], ["line_name"])
ax.set_ylabel("test")
ax.set_xlabel("test2")
ax.set_title("another title")

plt.show()
