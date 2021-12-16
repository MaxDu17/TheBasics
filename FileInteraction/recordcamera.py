import imageio as iio
import matplotlib.pyplot as plt
import time

#this shows how you might read from a webcam and display it in a matplotlib window

fig, ax = plt.subplots()
plt.ion()
reader = iio.get_reader('<video1>') #or video 0

for i in range(100):
    arr = reader.get_next_data() #this is the line you need
    print(arr.shape)
    #this is just for show
    ax.imshow(arr)
    plt.show()
    plt.pause(1e-6)
    time.sleep(0.1)
reader.close()
