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

### or you can just use a function and global variables
x_data = [1, 2, 3]
y_data = [1, 4, 5]
z_data = [2, 3, 4]

# this rotates the plot 
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_axis_off()
scat = ax.scatter3D(x_data, y_data, z_data, c=y_data, cmap='plasma')

angle = 0
def update(frame):
    global angle
    ax.view_init(20, angle, 0)
    angle += 3
    return (scat,)
import matplotlib.animation as animation

ani = animation.FuncAnimation(fig=fig, func=update, frames=120, interval=30)
ani.save("test.gif")
plt.show()