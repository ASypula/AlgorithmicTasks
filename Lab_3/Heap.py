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
    # results store results that will be added to file
    results_k2 = ""
    results_k3 = ""
    results_k4 = ""
    # prepare arrays to plot graph
    values_k2 = []
    values_k3 = []
    values_k4 = []
    keys_all = []
    while (i < amount):
        for x in range(1, n + 1):
            newEl = random.randint(0, 1000)
            arr.append(newEl)

        with open ("input.txt", 'a') as fh:
            fh.write(f'Number of elements: {n}\n')
            fh.write(str(arr))
            fh.write('\n\n\n')

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

        values_k2.append(timek2)
        keys_all.append(n)
        values_k3.append(timek3)
        values_k4.append(timek4)

        results_k2 += f'It took {timek2} seconds to make heap from {n} elements\n\n'
        print(f'It took {timek2} seconds to make heap from {n} elements\n\n')
        results_k3 += f'It took {timek3} seconds to make heap from {n} elements\n\n'
        print(f'It took {timek3} seconds to make heap from {n} elements\n\n')
        results_k4 += f'It took {timek4} seconds to make heap from {n} elements\n\n'
        print(f'It took {timek4} seconds to make heap from {n} elements\n\n')
        n = n + increase
        i = i + 1

    with open ("wyniki_heap_k2.txt", 'w') as fh:
        fh.write(results_k2)

    with open ("wyniki_heap_k3.txt", 'w') as fh:
            fh.write(results_k3)

    with open ("wyniki_heap_k4.txt", 'w') as fh:
            fh.write(results_k4)

    with open ("wyniki_all_heaps.txt", 'w') as fh:
        pass

    # time to plot
    for i in range (2,5):
        if i == 2:
            plt.plot(keys_all, values_k2, label = f'Heap {i}')
        elif i == 3:
            plt.plot(keys_all, values_k3, label = f'Heap {i}')
        else:
            plt.plot(keys_all, values_k4, label = f'Heap {i}')
        plt.title(label= f'Building heap times, k={i}')
        plt.xlabel("n")
        plt.ylabel("t [s]")
        plt.legend()
        plt.savefig(f'Heap_{i}_times.png')
        plt.axis([0, 11000, 0, 0.2])
        plt.clf()

    # final plotting - all heaps in one file
    plt.plot(keys_all, values_k2, label = 'Heap 2')
    plt.plot(keys_all, values_k3, label = 'Heap 3')
    plt.plot(keys_all, values_k4, label = 'Heap 4')
    plt.title(label= f'Building heap times')
    plt.xlabel("n")
    plt.ylabel("t [s]")
    plt.legend()
    plt.savefig(f'Heap_times_all.png')
def main():
    plot_graph_heaps(20, 500)


if __name__ == "__main__":
    main()
