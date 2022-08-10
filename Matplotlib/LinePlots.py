import matplotlib.pyplot as plt
import numpy as np
"""
This shows you how to plot a simple double line graph and shows off the legend feature 
"""
plt.rcParams["lines.linewidth"] = 3 # good practice to have thick lines 
# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# generate your simple setup
fig, ax = plt.subplots()

#plot two curves like this...
# line = ax.plot(t, s) #the main function
# line2 = ax.plot(t, s + 0.15) #the main function

#or like this!! (preferred method)
line, line2 = ax.plot(t, s, t, s + 0.15)

# here are some cool controls you can have
ax.set_ylabel("test")
ax.set_xlabel("test2")
ax.set_title("another title")
ax.set_xlim(0, 1) #set bounds
ax.set_ylim(0, 5)
line.set_color("teal") #example of how you use line

plt.legend([line, line2], ["line", "line 2"]) #more on this in a different sectoin

# gridline if needed
ax.grid()

fig.savefig("test.png")
fig.savefig("test.pdf") #save as pdf for paper-ready presentation
plt.show()