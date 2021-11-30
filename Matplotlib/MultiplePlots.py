import matplotlib.pyplot as plt

# generate your simple setup
fig, (ax1, ax2) = plt.subplots(ncols = 2)

plt.tight_layout() #helps with spacing--see what happens when you remove it

plt.title("I'm an overarching title") #this is the title of the whole window
ax1.set_title("I'm a competing title") #this usurps the previous title because ax is the same as plt and figure in this examle
ax2.set_title("I'm another title")

fig.savefig("test.png")
fig.savefig("test.pdf") #save as pdf for paper-ready presentation
plt.show()