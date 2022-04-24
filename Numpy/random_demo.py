import numpy as np

np.random.seed(1234)

x = np.random.choice([1, 2, 3], size = (2, 2), replace = True)
x = np.random.rand(2, 3)
x = np.random.randint(low = 2, high = 100, size = (2, 3))
# print(x)
