import imageio #need to install imageio_ffmpeg too

#audio is NOT saved!
im = imageio.get_reader("samples/sample.mp4")
fps = im.get_meta_data()['fps']
writer = imageio.get_writer("samples/samplea_written.mp4", fps=fps)
for frame in im:
    print('reading and writing')
    # print(frame.shape)
    writer.append_data(frame[:, :, 1]) #grayscale rendering
writer.close()
