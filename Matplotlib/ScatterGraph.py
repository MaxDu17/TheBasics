import matplotlib.pyplot as plt
import numpy as np

x_data = np.asarray([1, 2, 3])
y_data = [3, 5, 2]

fig, ax = plt.subplots()

#this is a demonstration of two bars. Feel free to remove one of the bars
scatter_object = ax.scatter(x_data, y_data, color = "blue", s = 10) #s is the size of the bubbles; it can be a list

ax.set_yticks(ticks = [1, 2, 3, 4, 5, 7]) #showing you what you can do with the ticks
ax.set_ylabel("test")
# plt.xticks(ticks = x_data, labels = x_labels) #you must ust the plt here
ax.set_xlabel("test2")
ax.set_title("another title")
# scatter_object.set_color("orange") #you can also set color this way

fig.savefig("test.png")
fig.savefig("test.pdf") #save as pdf for paper-ready presentation
plt.show()
