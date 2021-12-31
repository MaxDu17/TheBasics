import torch
from torch.utils.tensorboard import SummaryWriter
import numpy as np

writer = SummaryWriter('runs/test1') #you can specify logging directory

for epoch in range(10):
    loss = 10 - epoch #a dummy loss function
    writer.add_scalar("Loss/train", loss, epoch)
    x = np.random.random(1000) #generate a random vector of 1000 values
    writer.add_histogram('distribution centers', x + epoch, epoch)
    img = np.zeros((3, 100, 100))
    writer.add_image("my_image", img, epoch, dataformats = "CHW") #also accepts HWC, HW (greyscale)

    # here are a few more writer features taht could be useful later
    #writer.add_images("my_images", images, epoch) # displays multiple images in a grid
    # writer.add_figure("my_figure", matplotlib_figure, epoch)
    # writer.add_video("my video", vid_tensor, epoch) #requires moviepy
    # writer.add_audio("my audio", audio_tensor epoch, sample_rate = 44100)
    # writer.add_text("my text", "this is a test", epoch)
    # writer.add_graph(model, verbose = True, use_struct_trace = True) #show the computational graph
    # writer.add_embedding(data, global_step = epoch) # takes an NXD array, where N is data and D is dimemsion
    # writer.add_pr_curve("my PR curve", labels, predictions, epoch) # add precision recall curve
    # writer.add_hparams(hparam_dict, metric_dict


writer.flush()
writer.close()

