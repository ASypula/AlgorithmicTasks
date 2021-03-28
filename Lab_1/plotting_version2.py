import matplotlib.pyplot as plt
import time
import sys
import argparse
from selection_sort import selection_sort
from quick_sort import quick_sort
from bubble_sort import bubble_sort
from merge_sort import merge_sort
import string


def get_table(path, number):
    tab = []
    i = 0
    with open(path, 'r') as fp:
        text = fp.read()
        text = text.split()
        for word in text:
            if i < number:
                tab.append(word.strip(string.punctuation))
                i = i + 1
    return tab


def plot_graph_function(sort_function, numb, path, sort_func):
    keys = []
    value = []
    name = ["merge_sort", "bubble_sort", "quick_sort", "selection_sort"]
    if sort_function == quick_sort:
        for i in range(1, numb):
            tab = get_table(path, i*100)
            start = time.time()
            tab = sort_function(tab, 0, len(tab)-1)
            end = time.time()
            t = end-start
            value.append(t)
            keys.append(i * 100)
    else:
        for i in range(1, numb):
            tab = get_table(path, i*100)
            start = time.time()
            tab = sort_function(tab)
            end = time.time()
            t = end-start
            value.append(t)
            keys.append(i * 100)
    plt.plot(keys, value, label=name[sort_func])
    if sort_func == 3:
        plt.legend()
        plt.title(label="Sorting_functions.png")
        plt.savefig("all_functions.png")

    # to plot graph for each function separately
    # plt.plot(keys, value, label=name[sort_func])
    # plt.title(label=name[sort_func])
    # file_name = name[sort_func] + ".png"
    # plt.savefig(file_name)
    # plt.clf()


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE')

    # check if user gave input file name
    if len(arguments) != 2:
        print("Invalid number of arguments. You must give a file name")
    else:
        args = parser.parse_args(arguments[1:])
        path = args.FILE
        functions = [merge_sort, bubble_sort, quick_sort, selection_sort]
        for i in range(0, 4):
            # second argument - number of words to be sorted later multiplied by 100
            plot_graph_function(functions[i], 20, path, i)
        args = parser.parse_args(arguments[1:])


if __name__ == "__main__":
    main(sys.argv)
