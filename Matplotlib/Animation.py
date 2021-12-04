import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def beta_pdf(x, a, b):
    return (x**(a-1) * (1-x)**(b-1) * math.gamma(a + b)
            / (math.gamma(a) * math.gamma(b)))


class UpdateDist:
    def __init__(self, ax, prob=0.5):
        self.success = 0
        self.prob = prob
        self.line, = ax.plot([], [], 'k-') #initialize blank line
        self.x = np.linspace(0, 1, 200)
        self.ax = ax

        # Set up plot parameters
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 10)
        self.ax.grid(True)

    def __call__(self, i):
        #this following code segment is someting that updates the "y" array. Replace this
        if i == 0:
            self.success = 0
            self.line.set_data([], [])
            return self.line,
        if np.random.rand(1,) < self.prob:
            self.success += 1
        y = beta_pdf(self.x, self.success + 1, (i - self.success) + 1)


        self.line.set_data(self.x, y) #essentially you reset the line!
        return self.line, #this comma is very important


fig, ax = plt.subplots()
ud = UpdateDist(ax)
#interval is how long, and frames is number of frames
anim = FuncAnimation(fig, ud, frames=50, interval=50, blit=True)
anim.save("test.mp4", dpi=250, bitrate=8192)

plt.show()