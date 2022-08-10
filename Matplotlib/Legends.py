import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["lines.linewidth"] = 3
plt.rcParams["text.usetex"] = True # you can use latex typesetting in matplotlib
plt.rc("text.latex", preamble = r"\usepackage{amsmath}") # allows imports1

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
line, line2 = ax.plot(t, s, t, s + 0.3)

# better reference: https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot

plt.title("This is a plot")
# the "r" is very important.
plt.legend([line, line2], [r"line \textsc{Test}", r"line $N_{\text{test}}$"],
           bbox_to_anchor = (0.5, -0.1), # from lower left corner
           ncol = 2, fancybox = True, framealpha = 0.5)

fig.savefig("test.png", bbox_inches="tight") # doesn't cut off the legend
# fig.savefig("test.pdf", bbox_inches="tight") #save as pdf for paper-ready presentation
plt.show()