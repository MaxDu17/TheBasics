import matplotlib.pyplot as plt
import numpy as np
"""
This shows you how to plot a simple double line graph and shows off the legend feature 
"""

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# generate your simple setup
fig, ax = plt.subplots()

#plot two curves like this...
line = ax.plot(t, s, ls = "dashdot") #the main function

error = 0.3 #can be an array

plt.fill_between(t, s - error, s + error, alpha=0.2, edgecolor='#1B2ACC', facecolor='#089FFF',
    linewidth=4, linestyle='dashdot', antialiased=True)

# here are some cool controls you can have
ax.set_ylabel("test")
ax.set_xlabel("test2")
ax.set_title("another title")


plt.show()