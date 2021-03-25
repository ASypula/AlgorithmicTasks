import matplotlib.pyplot as plt
import timeit
import sys
import argparse


def get_table(path, number):
    with open(path, 'r') as fp:
        text = fp.read()
        tab = []
        count = 0
        word = ""
        for char in text:
            if (count < number):
                if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
                    word += char
                else:
                    if char == " ":
                        count = count + 1
                    if word != "":
                        tab.append(word)
                    word = ""
                    continue
            else:
                break
    return tab


def plot_graph(function_code, setup_code, numb, tab, path):
    keys = []
    value = []
    for i in range(1, numb):
        tab = get_table(path, i*10000)
        t = timeit.timeit(setup=setup_code, stmt=function_code, number=10000)
        value.append(t)
        keys.append(i*1000)
    plt.plot(keys, value, label=function_code)
    plt.title(label=f'{function_code}')
    plt.legend()
    plt.savefig(f'{function_code}.png')
    # plt.show()
    plt.clf()


def main(arguments):
    global tab
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE')

    # check if user gave input file name
    if len(arguments) != 2:
        print("Invalid number of arguments. You must give a file name")
    else:
        args = parser.parse_args(arguments[1:])
        path = args.FILE
        setup = [setup_quick, setup_selection, setup_merge, setup_bubble]
        algorithm = [sort_quick, sort_selection, sort_merge, sort_bubble]
        tab = get_table(path, 10)

        for i in range(0, 4):
            plot_graph(algorithm[i], setup[i], 10, tab, path)
        args = parser.parse_args(arguments[1:])


setup_selection = '''
from selection_sort import selection_sort
from __main__ import tab '''

sort_selection = '''
selection_sort(tab)
'''

setup_quick = '''
from quick_sort import quick_sort
from __main__ import tab'''

sort_quick = "quick_sort(tab, 0, len(tab)-1)"

setup_bubble = '''
from bubble_sort import bubble_sort
from __main__ import tab'''

sort_bubble = '''
bubble_sort(tab)'''

setup_merge = '''
from merge_sort import merge_sort
from __main__ import tab'''

sort_merge = '''
merge_sort(tab)'''

if __name__ == "__main__":
    main(sys.argv)
