from matplotlib import pyplot as plt

plt.rcParams["lines.linewidth"] = 3
plt.rcParams["text.usetex"] = True # you can use latex typesetting in matplotlib
plt.rc("text.latex", preamble = r"\usepackage{amsmath}") # allows imports

plt.plot((1, 2, 3))
plt.ylabel("test $2x$")
plt.xlabel("The $\int_a^b$ plot")
plt.show()