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
# line = ax.plot(t, s, ls = "dashdot") #the main function

#or use the format string (which is really nice)
line = ax.plot(t, s, 'k*') #the main function
#markers, then line style, then color
#Markers:
# . , o v ^ < > 1 2 3 4 8 s p P * h H + x X D d | _
#line styles
# - -- -. :
#colors
# b g r c m y k w

# here are some cool controls you can have
ax.set_ylabel("test")
ax.set_xlabel("test2")
ax.set_title("another title")


plt.show()