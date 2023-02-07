# this file looks into the communal results direcotry and generates the appropiate statistics and plots.
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import argparse
import csv
from matplotlib.pyplot import figure
######### REQUIRED FILE STRUCTURE ######
# Assume that all results are found within one outer directory
# Assume that all seeds are writen under the same prefix, like my_run_seed10, my_run_seed20, etc
# Assume that these are all folders, and inside the folder there is a file with a consistent name, like data.csv

# for high-visibility analysis purposes, don't use the --display flag. For good visual properties (like for posters and papers), use the display flag
##############################

# from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
# rc('font',**{'family':'serif','serif':['Times']})
# rc('text', usetex=True)

def read_file_group(dir_list, file_name, counter, value):
    """
    This function takes in a list of directories and computes the statistics for them
    :param dir_list: list of directories, corresponding to one type of run
    :param file_name: the name of a logging file that is common in all of them
    :return: list of numpy arrays, each a trajectory. Also returns an index array of the longest trajectory
    """

    success_rates = list()
    for dir in sorted(dir_list):
        try:
            files = os.listdir(dir)
            file_name = [k for k in files if "success_rate" in k][0] # janky but extracts the relevant file
            with open(f"{dir}/{file_name}", "r") as f:
                success_rates.append(float(f.readline()))
            print(f"\tSuccessfully parsed {dir}")
        except Exception as e:
            print(f"\tSkipped {dir} due to {e}")
    return success_rates

def display_format(colors, ax, x_label = "x", y_label="y", title = "title", no_label = False):
    # ax.set_facecolor(colors["background"])
    # ax.grid(color=colors["grid"], linewidth=0.7)

    ax.spines["bottom"].set_color(colors["ax"])
    ax.spines["bottom"].set_linewidth(1)
    ax.spines["left"].set_color(colors["ax"])
    ax.spines["left"].set_linewidth(1)
    ax.spines["right"].set_linewidth(0)
    ax.spines["top"].set_linewidth(0)

    if not no_label:
        # ax.set_xlabel(x_label, fontdict={"color": colors["text"]}, labelpad=7.0)
        ax.set_ylabel(y_label, fontdict={"color": colors["text"]}, labelpad=2, fontname= "sans-serif", fontsize = 10)
        ax.set_title(title, fontdict={"color": colors["text"]}, fontname= "sans-serif", fontsize = 12)

    ax.tick_params(axis="x", colors=colors["ax"], labelsize="small")
    ax.tick_params(axis="y", colors=colors["ax"], labelsize=14)

    # plt.tick_params(
    #     axis='x',  # changes apply to the x-axis
    #     which='both',  # both major and minor ticks are affected
    #     labelsize = 14)

    [t_label.set_color(colors["text"]) for t_label in ax.xaxis.get_ticklabels()]
    [t_label.set_color(colors["text"]) for t_label in ax.yaxis.get_ticklabels()]


def plot_correction_progress(args):
    # fig, ax = plt.subplots(figsize=(8, 3))
    fig, ax = plt.subplots(figsize=(5, 3.5))
    fig.subplots_adjust(bottom=0.1)
    if not args.display:
        color_list = ["blue", "green", "purple", "brown", "orange", "olive"]
        # plt.grid()
        plt.style.use("seaborn")
        ax.set_ylabel("Success Rate")
        # ax.set_xlabel(args.xlabel)
        ax.set_title(args.title)
    else:
        # color_list = ["#FF6150","#134E6F", "#1AC0C6", "#FFA822", "#FF4AEA"]
        color_list = args.colors #["#404040", "#ff4c38", "#3899a8", "#daa049", "#99ae32", "#368745", "#b38ec7", "#8b3c6d"]
        # color_list = ["#134E6F", "#FF6150", "#1AC0C6", "#FFA822", "#BDE200", "#00C725", "#C559FF", "#C09007C"]

        colors = {
            "background": "#f7fbfb",
            "grid": "#eef2f3",
            # "ax": "#c8c8d3",
            "ax": "#000000",
            # "text": "#6e6e80"
            "text": "#000000"
        }
        no_label = False
        plt.style.use("ggplot")
        display_format(colors, ax, "Methods", "Success Rate", args.title, no_label)


    # modifier is the subdirectory to use under the main directory.


    y_data_1 = list()
    y_data_2 = list()
    err_1 = list()
    err_2 = list()
    x_data = np.array([0, 0.8])
    # ordered_names = ["SELECT (ours)", "EXP", "GC", "BB"] #CHANGE THIS TO ADD MORE
    ordered_names = ["ORACLE", "SELECT (ours)", "EXP", "BB", "GC", "GCFT"] #CHANGE THIS TO ADD MORE

    current_dir = os.getcwd()
    os.chdir(args.base_dir_1)
    file_names = os.listdir()
    for elem in args.plots_1:
        relevant_runs = [file for file in file_names if file.startswith(elem) and ".hdf5" not in file] #sort prefixes
        vals = read_file_group(relevant_runs, args.logging_file, args.counter, args.value)
        y_data_1.append(np.mean(vals))
        err_1.append(np.std(vals) / (np.sqrt(len(vals))))

    if args.base_dir_2 is not None:
        os.chdir(current_dir)
        os.chdir(args.base_dir_2)
        file_names = os.listdir()

        for elem in args.plots_2:
            relevant_runs = [file for file in file_names if file.startswith(elem) and ".hdf5" not in file] #sort prefixes
            vals = read_file_group(relevant_runs, args.logging_file, args.counter, args.value)
            y_data_2.append(np.mean(vals))
            err_2.append(np.std(vals) / (np.sqrt(len(vals))))

        os.chdir(current_dir)
        os.chdir("./final_plots/")
        with open(f"{args.title}_state.csv", "w") as f:
            write = csv.writer(f)
            write.writerow(["method", "success_rate", "error"])
            for i, (rate, error) in enumerate(zip(y_data_2, err_2)):
                write.writerow([ordered_names[i], rate, error])

        with open(f"{args.title}_image.csv", "w") as f:
            write = csv.writer(f)
            write.writerow(["method", "success_rate", "error"])
            for i, (rate, error) in enumerate(zip(y_data_1, err_1)):
                write.writerow([ordered_names[i], rate, error])

        for i in range(len(y_data_1)):
            # combined = [y_data_1[i], 0]
            # combined_err = [err_1[i], 0]
            combined = [y_data_1[i], y_data_2[i]]
            combined_err = [err_1[i], err_2[i]]
            color = color_list[(i) % len(color_list)]
            if color != "HATCH":
                ax.bar(x_data + i * 0.15, combined, width=0.15, color=color, label=ordered_names[i])
            else:
                ax.bar(x_data + i * 0.15, combined, width=0.15, fill=False, edgecolor='black', hatch='xx', label=ordered_names[i])

            # ax.bar(x_data + i * 0.15, combined, width=0.15, color=color_list[i], label = ordered_names[i])
            ax.errorbar(x_data + i * 0.15, combined, yerr=combined_err, fmt='none', ecolor="#000000", capsize=2)
        plt.xticks(ticks=x_data + 0.15 * (len(y_data_1) - 1) / 2, labels=["Image", "State"])
    else:
        # single run
        os.chdir(current_dir)
        os.chdir("./final_plots/")
        with open(f"{args.title}_state.csv", "w") as f:
            write = csv.writer(f)
            write.writerow(["method", "success_rate", "error"])
            for i, (rate, error) in enumerate(zip(y_data_1, err_1)):
                write.writerow([ordered_names[i], rate, error])

        for i in range(len(y_data_1)):
            ax.bar(i * 0.15, [y_data_1[i]], width=0.15, color=color_list[i], label=ordered_names[i])
            ax.errorbar(i * 0.15, [y_data_1[i]], yerr=[err_1[i]], fmt='none', ecolor="#000000", capsize=2)

        # plt.xticks(ticks = x_data + 0.15 * (len(y_data_1 ) - 1) / 2, labels = ["State"])

    # ax.legend(loc = "lower center", bbox_to_anchor=(0.5, -0.12), ncol = 6, framealpha=.9, facecolor='white')
    # automatic scaling
    fig.savefig(f"{args.title}.png", dpi = 200)
    fig.savefig(f"{args.title}.pdf")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--colors',
        nargs='+',
        help='the names of your runs (assumed prefixes)',
        required=True)
    # Dataset path, to override the one in the config
    parser.add_argument(
        "--base_dir_1",
        type=str,
        default="./",
        required=True,
        help="where all the logs are stored. Use a relative address or an absolute address",
    )
    parser.add_argument(
        '--plots_1',
        nargs='+',
        help='the names of your runs (assumed prefixes)',
        required=True)
    # Use like:
    # python arg.py -l 1234 2345 3456 4567

    # Dataset path, to override the one in the config
    parser.add_argument(
        "--base_dir_2",
        type=str,
        default=None,
        required=False,
        help="where all the logs are stored. Use a relative address or an absolute address",
    )
    parser.add_argument(
        '--plots_2',
        nargs='+',
        help='the names of your runs (assumed prefixes)',
        default = None,
        required=False)

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
    plot_correction_progress(args)
