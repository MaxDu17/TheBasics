from matplotlib import pyplot as plt

# this is the object-oriented way of doing things
fig, ax = plt.subplots()
ax.plot((1, 2, 3))
plt.show()
# object oriented allows you to keep track of many plots and individual styles. However, the downside is that it can be bulky.

# this is the direct way of doing things
plt.plot((1, 2, 3))
plt.show()
# direct plotting allows you to do simple plots without worrying keeping track of objects. The downside is that we can't do
# things like multi-axis plots, etc

# by default, in this repository and in general, you should be using object-oriented unless you're only plotting one thing.