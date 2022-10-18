batch = []


from matplotlib import pyplot as plt
import numpy as np
# batch is your batch
anchor = batch[0].cpu().detach().numpy()
fig, ax = plt.subplots()
ax.imshow(np.transpose(anchor, (1, 2, 0)))
plt.savefig("train.png")
