import matplotlib.pyplot as plt

# generate your simple setup
fig, (ax1, ax2) = plt.subplots(ncols = 2) #, figsize = (7, 7)) #use figure size to manually control how large the plot will be, in inches


plt.title("I'm an overarching title") #this is the title of the whole window
ax1.set_title("I'm a competing title") #this usurps the previous title because ax is the same as plt and figure in this examle
ax2.set_title("I'm another title")

#adjusts the spacing. The top, bottom, left, and right are proportions. So top=.92 means that the top is 92% of the length from the bottom edge to the top edge, etc
# plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
plt.tight_layout(pad = 0.4, w_pad = 1.0, h_pad = 1.0) # "pad" is between figure and subplot edge, and w_pad / h_pad is between subplots

# fig.subplots_adjust(hspace=0.3) # another way of doing it

fig.savefig("test.png")
fig.savefig("test.pdf") #save as pdf for paper-ready presentation

plt.show()