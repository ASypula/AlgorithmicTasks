import matplotlib.pyplot as plt
import timeit

global tab

def get_table(name, number):
    with open(name, 'r') as fp:
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


def plot_graph(function_code, setup_code, numb, tab):
    # table = []
    keys = []
    value = []
    for i in range(1, numb):
        tab = get_table("pan-tadeusz.txt", i*1000)
        t = timeit.timeit(setup=setup_code, stmt=function_code, number=100000)
        print(t)
        value.append(t)
        keys.append(i*1000)
        # table.append(t)
    # print(tab)
    plt.plot(keys, value, label=function_code)
    plt.title(label=function_code)
    plt.savefig(f'{function_code[:5]}.png')
    # plt.show()
    plt.clf()  # jak sie to usunie to bedzie wykres ze wszystkim na raz


tab = get_table("pan-tadeusz.txt", 10)


setup_insert = '''
from Sort import insertion_sort
from __main__ import tab '''

sort_insertion = '''
insertion_sort(tab)
'''

setup_quick = '''
from Sort import quick_sort
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

setup = [setup_quick, setup_insert, setup_merge, setup_bubble]

algorithm = [sort_quick, sort_insertion, sort_merge, sort_bubble]

for i in range(0, 4):
    print(f"Now:{algorithm[i]} ")
    plot_graph(algorithm[i], setup[i], 10, tab)
