
import pandas as pd
import matplotlib.pyplot as plt

def main():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    df = pd.read_csv("data/" + "tsne.csv")
    projection = df.to_numpy()
    df = pd.read_csv("data/" + "labels.csv")
    labels = df.to_numpy()[:, 0]

    # ax.plot(projection[:, 0], projection[:, 1], color='green', marker='o', markersize = 3)

    indices_successful = labels == 1
    ax.scatter(projection[indices_successful, 0], projection[indices_successful, 1], projection[indices_successful, 2],color='green', s = 1)
    indices_unsuccessful = labels == 0
    ax.scatter(projection[indices_unsuccessful, 0], projection[indices_unsuccessful, 1], projection[indices_unsuccessful, 2], color='red', s = 1)
    plt.savefig("test.png")
    plt.show()

main()