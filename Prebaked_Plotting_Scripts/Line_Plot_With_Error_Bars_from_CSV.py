# this file looks into the communal results direcotry and generates the appropiate statistics and plots.
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import argparse


#### THIS FILE NEEDS CLEAN-UP WORK ####


######### REQUIRED FILE STRUCTURE ######
# Assume that all results are found within one outer directory
# Assume that all seeds are writen under the same prefix, like my_run_seed10, my_run_seed20, etc
# Assume that these are all folders, and inside the folder there is a file with a consistent name, like data.csv

# for high-visibility analysis purposes, don't use the --display flag. For good visual properties (like for posters and papers), use the display flag
##############################

def read_file_group(dir_list, file_name, counter, value):
    """
    This function takes in a list of directories and computes the statistics for them
    :param dir_list: list of directories, corresponding to one type of run
    :param file_name: the name of a logging file that is common in all of them
    :return: list of numpy arrays, each a trajectory. Also returns an index array of the longest trajectory
    """
    file_list = list()
    index = []
    for dir in sorted(dir_list):
        try:
            df = pd.read_csv(f"{dir}/{file_name}")
            file_list.append(df[value].to_numpy())
            index = df[counter] if len(df[counter]) > len(index) else index #these are the steps
            print(f"\tSuccessfully parsed {dir}")
        except Exception as e:
            print(f"\tSkipped {dir} due to {e}")
    return file_list, index

# a more aggressive smoothing option
def running_mean(scalars):
    smoothed = list()
    smoothed.append(scalars[0])
    for i in range(1, len(scalars)):
        smoothed.append(np.mean(scalars[0 : i]))
    return np.asarray(smoothed)

# smoothing
def smooth(scalars, weight):
    last = scalars[0]  # First value in the plot (first timestep)
    smoothed = list()
    for point in scalars:
        smoothed_val = last * weight + (1 - weight) * point  # Calculate smoothed value
        smoothed.append(smoothed_val)  # Save it
        last = smoothed_val  # Anchor the last smoothed value

    return np.asarray(smoothed)


def display_format(colors, ax, x_label="x", y_label="y", title = "title", no_label = False):
    ax.set_facecolor(colors["background"])
    # ax.grid(color=colors["grid"], linewidth=0.7)

    ax.spines["bottom"].set_color(colors["ax"])
    ax.spines["bottom"].set_linewidth(1)
    ax.spines["left"].set_color(colors["ax"])
    ax.spines["left"].set_linewidth(1)
    ax.spines["right"].set_linewidth(0)
    ax.spines["top"].set_linewidth(0)

    if not no_label:
        ax.set_xlabel(x_label, fontdict={"color": colors["text"]}, labelpad=7.0)
        ax.set_ylabel(y_label, fontdict={"color": colors["text"]}, labelpad=7.0)
        ax.set_title(title, fontdict={"color": colors["text"]})

    # ax.tick_params(axis="x", colors=colors["ax"], labelsize="large")
    # ax.tick_params(axis="y", colors=colors["ax"], labelsize="large")
    ax.tick_params(axis="x", colors=colors["ax"], labelsize=18)
    ax.tick_params(axis="y", colors=colors["ax"], labelsize=18)

    [t_label.set_color(colors["text"]) for t_label in ax.xaxis.get_ticklabels()]
    [t_label.set_color(colors["text"]) for t_label in ax.yaxis.get_ticklabels()]


def plot_correction_progress(args):
    color_index = 0
    fig, ax = plt.subplots()

    XLABEL = args.xlabel #"Intervention Episodes"
    YLABEL = "Suceess Proportion"
    TITLE = args.title #"Success vs. Interventions"

    if not args.display:
        color_list = ["blue", "green", "purple", "brown", "orange", "olive"]
        # plt.grid()
        plt.style.use("seaborn")
        ax.set_ylabel(YLABEL)
        ax.set_xlabel(XLABEL)
        ax.set_title(TITLE)
    else:
        # color_list = "#404040", "#ff4c38", "#3899a8", "#daa049", "#99ae32", "#368745", "#b38ec7", "#8b3c6d"
        color_list = "#7f7f7f", "#ff6150", "#74bde7", "#e9c48b", "#7cc763", "#63c7a4"
        # color_list = ["#FF6150","#134E6F", "#1AC0C6", "#FFA822", "#091A29",  "#FF4AEA"]
        colors = {
            "background": "#ffffff",
            "grid": "#eef2f3",
            # "ax": "#c8c8d3",
            "ax": "#000000",
            # "text": "#6e6e80"
            "text": "#000000"
        }
        no_label = True
        plt.style.use("ggplot")
        display_format(colors, ax, XLABEL, YLABEL, TITLE, no_label)


    # modifier is the subdirectory to use under the main directory.
    file_names = os.listdir()
    smooth_amount = args.smoothing

    if args.baseline is not None:
        idx = np.arange(args.limit)
        vals = np.ones_like(idx) * args.baseline
        ax.plot(idx, vals, color = "#1100ad")
        ax.fill_between(idx, vals - args.baseline_margin, vals + args.baseline_margin, alpha=0.1,
                        facecolor = "#1100ad",
                        linewidth=0, antialiased=True)
    val_min = 1
    val_max = 0 #initialize the bounds
    for elem in args.plots:
        if elem == "DUMMY": #allows you to skip a color for consistency without having the plot
            color_index += 1
            continue
        relevant_runs = [file for file in file_names if file.startswith(elem) and ".hdf5" not in file] #sort prefixes
        vals, idx = read_file_group(relevant_runs, args.logging_file, args.counter, args.value)

        # make a list of means and standard deviations
        mean_list = list()
        stdev_list = list()
        for i in range(len(idx)):
            step_list = list()
            for trajectory in vals:
                if i < trajectory.shape[0]:
                    step_list.append(trajectory[i])
            mean_list.append(np.mean(step_list))
            stdev_list.append(np.std(step_list) / ( np.sqrt(len(step_list))))
        val_min = np.min(smooth(mean_list, smooth_amount)) if np.min(smooth(mean_list, smooth_amount)) < val_min else val_min
        val_max = np.max(smooth(mean_list, smooth_amount)) if np.max(smooth(mean_list, smooth_amount)) > val_max else val_max
        if color_list[color_index] == "#7f7f7f":
            ax.plot(idx, smooth(mean_list, smooth_amount), "--", color = color_list[color_index], label = elem)
        else:
            ax.plot(idx, smooth(mean_list, smooth_amount), color = color_list[color_index], label = elem)
        ax.fill_between(idx, smooth([m - s for m, s in zip(mean_list, stdev_list)], smooth_amount),  smooth([m + s for m, s in zip(mean_list, stdev_list)], smooth_amount), alpha=0.1,
                        facecolor = color_list[color_index],
                         linewidth=0, antialiased=True)
        if not args.display:
            ax.legend()
        color_index += 1
        color_index %= len(color_list)

    # automatic scaling
    ax.set_ylim(max(val_min - 0.05, 0), min(val_max + 0.05, 1))
    ax.set_xlim(args.burn_in, args.limit)
    fig.savefig(args.file_name, dpi = 200)
    fig.savefig("corrections_plot.pdf")
    # print(args.file_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Dataset path, to override the one in the config
    parser.add_argument(
        "--base_dir",
        type=str,
        default="./",
        required=False,
        help="where all the logs are stored. Use a relative address or an absolute address",
    )
    parser.add_argument(
        '-l',
        '--plots',
        nargs='+',
        help='the names of your runs (assumed prefixes)',
        required=True)
    # Use like:
    # python arg.py -l 1234 2345 3456 4567

    parser.add_argument(
        "--baseline",
        type=float,
        default=None,
        help="a horizontal baseline to display",
    )

    parser.add_argument(
        "--display",
        action='store_true',
        help="if in display mode, do not display legend or titles or use seaborn style, for cleaniness",
    )

    parser.add_argument(
        "--baseline_margin",
        type=float,
        default=None,
        help="a error bars on the baseline to display",
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=100,
        help="how many points you want to plot",
    )

    parser.add_argument(
        "--burn_in",
        type=int,
        default=0,
        help="burn-in steps (to ignore in the plot)",
    )

    parser.add_argument(
        "--smoothing",
        type=float,
        default=0.5,
        help="how much to smooth the plot",
    )

    parser.add_argument(
        "--logging_file",
        type=str,
        default='corrections.csv',
        help="the name of the logging file in each directory",
    )

    parser.add_argument(
        "--file_name",
        type=str,
        default='corrections_plot.png',
        help="the name of the output file in each directory",
    )

    parser.add_argument(
        "--counter",
        type=str,
        default="Correction",
        required=False,
        help="The value that you use to keep as an index between runs",
    )

    parser.add_argument(
        "--value",
        type=str,
        default="Success Rate",
        required=False,
        help="The value that you're monitoring",
    )

    parser.add_argument(
        "--title",
        type=str,
        default="Successes vs. Interventions",
        required=False,
        help="graph title",
    )

    parser.add_argument(
        "--xlabel",
        type=str,
        default="Intervention Episodes",
        required=False,
        help="x axis title",
    )


    args = parser.parse_args()
    os.chdir(args.base_dir)
    plot_correction_progress(args)
