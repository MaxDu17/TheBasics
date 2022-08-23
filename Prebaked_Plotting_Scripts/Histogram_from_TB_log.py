# use this tool: https://tbparse.readthedocs.io/en/latest/pages/parsing-histograms.html#plotting-multiple-stacked-distributions
import matplotlib.pyplot as plt
from tbparse import SummaryReader
import seaborn as sns
import numpy as np

log_dir = "data/events.out.tfevents"
EVERY_N = 10
START = 10
END = 100
HISTOGRAM_NAME = "Train/Sample_Distribution"

reader = SummaryReader(log_dir, pivot=True)
df = reader.histograms

df = df[START:END:EVERY_N]
plt.figure(figsize=(15, 15)) # width and height in inches
# Set background
sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})
# Choose color palettes for the distributions
pal = sns.color_palette("Oranges", 20)[5:-5]
# Initialize the FacetGrid object (stacking multiple plots)
g = sns.FacetGrid(df, row='step', hue='step', aspect=15, height=.4, palette=pal)

def plot_subplots(x, color, label, data):
    ax = plt.gca()
    ax.text(-0.02, .1, label, fontweight="bold", color=color,
          ha="right", va="center", transform=ax.transAxes)

    counts = data[f"{HISTOGRAM_NAME}/counts"].iloc[0]
    limits = data[f"{HISTOGRAM_NAME}/limits"].iloc[0]

    x = np.linspace(limits[0], limits[-1], 15)
    x, y = SummaryReader.histogram_to_pdf(counts, limits, x)
    # Draw the densities in a few steps
    sns.lineplot(x=x, y=y, clip_on=False, color="w", lw=2)
    ax.fill_between(x, y, color=color)

g.fig.suptitle('Main Title')
g.map_dataframe(plot_subplots, None)

# Add a bottom line for each subplot
# passing color=None to refline() uses the hue mapping
g.refline(y=0, linewidth=2, linestyle="-", color=None, clip_on=False)

# Set the subplots to overlap (i.e., height of each distribution)
g.figure.subplots_adjust(hspace=-.8)

# Remove axes details that don't play well with overlap
g.set_titles("")
g.set(yticks=[], xlabel="X title here", ylabel="") #leave ylabel blank
g.despine(bottom=True, left=True)

plt.savefig("test.png")
plt.show()

print("done")