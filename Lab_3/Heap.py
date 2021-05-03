import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt_delete
from time import process_time
import random
from Build_heap import buildHeapInsertion


def plot_graph_heaps(amount, increase):  #amount - number of repetitions, increase - how many more numbers we are adding each time to the list with random numbers
    i = 0
    n = increase
    arr = []
    heap = []
    # results[] store results that will be added to file
    results_k2 = []
    results_k3 = []
    results_k4 = []
    while (i < amount):
        for x in range(1, n + 1):
            newEl = random.randint(0, 1000)
            arr.append(newEl)
        start1 = process_time()
        heap = buildHeapInsertion(arr, 2)
        stop1 = process_time()
        start2 = process_time()
        heap = buildHeapInsertion(arr, 3)
        stop2 = process_time()
        start3 = process_time()
        heap = buildHeapInsertion(arr, 4)
        stop3 = process_time()
        timek2 = stop1 - start1
        timek3 = stop2 - start2
        timek4 = stop3 - start3

        n = n + increase
        i = i + 1

    with open ("wyniki_heap_k2.txt", 'w') as fh:
        for line in results_k2:
            fh.write(line)
            fh.write('\n')

    with open ("wyniki_heap_k3.txt", 'w') as fh:
            for line in results_k3:
                fh.write(line)
                fh.write('\n')

    with open ("wyniki_heap_k4.txt", 'w') as fh:
            for line in results_k4:
                fh.write(line)
                fh.write('\n')

    with open ("wyniki_all_heaps.txt", 'w') as fh:


def main():
    plot_graph_heaps(20, 500)


if __name__ == "__main__":
    main()
