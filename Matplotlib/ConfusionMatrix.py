import numpy as np
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

arr = np.asarray([
    [20, 8, 0],
    [1, 20, 0],
    [0, 0, 30]
])

#for primitive confusion matrix, use this:
# plt.matshow(arr)
# plt.show()
# quit()

#but that's kinda boring. Let's add more features!
labels = ["felix", "faizan", "elizabeth"]

df_cm = pd.DataFrame(arr, labels, labels)
plt.figure(figsize=(8,6))
sn.set(font_scale=1) # for label size
sn.heatmap(df_cm, annot=True, annot_kws={"size": 10}) # font size

plt.show()
plt.savefig("test.png")
plt.savefig("test.pdf")