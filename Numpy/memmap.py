import numpy as np

# write mode memmap
fp = np.memmap("test.mem", dtype='float32', mode='w+', shape=(3,4))
fp[:] = np.ones((3, 4))
fp.flush() # write the information to disk
print(fp)

try:
    fpr = np.memmap("test.mem", dtype='float32', mode='r', shape=(3,4)) #copy on write, meaning that you can edit this, but it doens't modify the original file
    fpr[0, 0] = 100 #illefal
    print(fpr)
except:
    print("verified read-only!")


fpc = np.memmap("test.mem", dtype='float32', mode='c', shape=(3,4)) #copy on write, meaning that you can edit this, but it doens't modify the original file
fpc[0, 0] = 100 #allowed
print(fpc)
