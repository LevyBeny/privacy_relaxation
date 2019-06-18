import matplotlib.pyplot as plt
import pandas as pd
import os
import re


def _plot_graph(file_path, title, df):
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(13, 10))
    plt.subplots_adjust(hspace=0.3)
    fig.suptitle(title.capitalize(), fontsize=20)

    df[['plan_length']].plot(ax=axes[0], color='b', marker='o')
    axes[0].set_title("Plan Length")
    df[['makespan']].plot(ax=axes[1], color='r', marker='*')
    axes[1].set_title("Makespan")
    df[['time']].plot(ax=axes[2], color='g', marker='^')
    axes[2].set_title("Time to Solve (sec)")

    plt.savefig(file_path)


algo = 'per_agent'
results_path = './{}_results'.format(algo)

# Loop over all results in for the given algorithm results path
for res_file in os.listdir(os.fsencode(results_path)):
    res_name = os.fsdecode(res_file)
    df = pd.read_csv(results_path + '/' + res_name,
                     names=['x', 'is_success', 'plan_length', 'makespan', 'time'])

    problem = re.sub('\.txt', '', res_name)
    _plot_graph('./graphs/{}/{}.png'.format(algo, problem), problem, df)
