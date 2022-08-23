from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

plt.figure(1)
plt.plot([1, 2, 3])
plt.figure(2)
plt.scatter((1, 2, 2), (1, 4, 2))

pp = PdfPages("test.pdf")
fig_nums = plt.get_fignums()
figs = [plt.figure(n) for n in fig_nums]
for fig in figs:
    fig.savefig(pp, format='pdf')
pp.close()