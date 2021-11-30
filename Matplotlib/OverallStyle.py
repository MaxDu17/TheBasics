import matplotlib.pyplot as plt

#leave this blank by default
plt.style.use("default")
# plt.style.use("seaborn")
# plt.style.use("default")
# plt.style.use("classic")
# plt.style.use("grayscale")
# plt.style.use("seaborn-notebook")

# generate your simple setup
fig, ax = plt.subplots()

# in general, fig and plt are the same thing. But ax is a singular plot

plt.title("I'm an overarching title") #this is the title of the whole window
ax.set_title("I'm a competing title") #this usurps the previous title because ax is the same as plt and figure in this examle

fig.savefig("test.png")
fig.savefig("test.pdf") #save as pdf for paper-ready presentation
plt.show()