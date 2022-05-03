import matplotlib.pyplot as plt
import numpy as np

distribution = np.random.randn(2000)

plt.hist(distribution, 50, density=True, facecolor='b', alpha=1) # should show a bell curve
plt.show()
