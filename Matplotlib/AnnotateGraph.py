import matplotlib.pyplot as plt
import numpy as np

ax = plt.subplot()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)
ax.set_ylim(-2, 2)

#here we exercise all different sorts of annotation powers

ax.text(3, 1.5, r"$\sigma \sum_{x = 0}^\infty f(x)$  test")

ax.annotate('test', xy=(2, 1), xytext=(2, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )
ax.grid()
ax.legend([line], ["line_name"])
ax.set_ylabel("test")
ax.set_xlabel("test2")
ax.set_title("another title")

plt.show()