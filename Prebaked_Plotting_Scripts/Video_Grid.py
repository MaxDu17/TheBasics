import imageio
import os
import numpy as np
import tqdm
import random

BASE_DIR = "../datasets/bridge/videos_pickle_cup"
SAVE_DIR = "video_grids/pickle_horiz.gif"

# BASE_DIR = "../datasets/bridge/videos_sink"
# SAVE_DIR = "video_grids/sink_horiz.gif"

# BASE_DIR = "../datasets/widowx_peg_paired"
# SAVE_DIR = "video_grids/peg_horiz.gif"

# BASE_DIR = "../datasets/widowx_peg_paired"
# SAVE_DIR = "video_grids/ours_peg_horiz.gif"

# BASE_DIR = "../datasets/bridge_own"
# SAVE_DIR = "video_grids/ours_pickle.gif"

# BASE_DIR = "../datasets/bridge_sink"
# SAVE_DIR = "video_grids/ours_sink.gif"

HEIGHT = 6
WIDTH = 4

# HEIGHT = 3
# WIDTH = 3

files = [k for k in os.listdir(BASE_DIR) if "gif" in k]

# files.sort(key = lambda x : int((x.split("demo")[1]).split(".")[0]))
assert len(files) > HEIGHT * WIDTH

video_list = list()
random.shuffle(files)
files = files[ : HEIGHT * WIDTH]

#audio is NOT saved!
for file in files:
    im = list(imageio.get_reader(f"{BASE_DIR}/{file}"))
    video_list.append(im)

# video_list = video_list[:HEIGHT * WIDTH]

longest = max([len(x) for x in video_list])
for video in video_list:
    last_frame = video[-1]
    while len(video) < longest:
        video.append(last_frame)

writer = imageio.get_writer(SAVE_DIR)
for i in tqdm.tqdm(range(longest)):
    col_list = list()
    for k in range(HEIGHT):
        row_list = list()
        for j in range(WIDTH):
            row_list.append(video_list[k * WIDTH + j][i])
        row = np.concatenate(row_list, axis = 0)
        col_list.append(row)
    whole_image = np.concatenate(col_list, axis = 1)
    writer.append_data(whole_image)

writer.close()
