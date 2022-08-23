import matplotlib.pyplot as plt
import time
import numpy as np


fig, ax = plt.subplots()
plt.ion() #needed to prevent show() from blocking

#this can skip a few frames; it is not meant to be particularly smooth
for i in range(25):
    print(i)
    ax.clear()
    arr = np.random.randint(0, 255, size=(100, 100, 3))
    ax.imshow(arr)
    ax.set_title(f"Iteration {i}")
    plt.show()
    plt.pause(1e-6) #this is a necessary thing
    time.sleep(0.5)