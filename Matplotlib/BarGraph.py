import matplotlib.pyplot as plt
import numpy as np

x_data = np.asarray([1, 2, 3])
x_labels = ["bear", "cat", "dog"]
y_data = [3, 5, 2]

fig, ax = plt.subplots()

#this is a demonstration of two bars. Feel free to remove one of the bars
bar_object = ax.bar(x_data - 0.15, y_data, width = 0.3)
bar_object2 = ax.bar(x_data + 0.15, y_data, width = 0.3) #you can also use a list of categories as the x_data
#this is a demonstration of the error bar feature. Feel free to remove
error_bars = ax.errorbar(x_data - 0.15, y_data, yerr = [1, 1, 1], fmt = 'none', ecolor="red", capsize = 2)
ax.set_yticks(ticks = [1, 2, 3, 4, 5, 7]) #showing you what you can do with the ticks
ax.set_ylabel("test")
plt.xticks(ticks = x_data, labels = x_labels) #you must ust the plt here
ax.set_xlabel("test2")
ax.set_title("another title")
bar_object[0].set_color("orange") #sets the first bar orange

fig.savefig("test.png")
fig.savefig("test.pdf") #save as pdf for paper-ready presentation
plt.show()
