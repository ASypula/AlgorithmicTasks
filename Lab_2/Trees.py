import matplotlib.pyplot as plt
from time import process_time
import random
import BST


def plot_graph_create_tree(amount, increase):  #amount - number of repetitions, increase - how many more numbers we are adding each time to the list with random numbers
    i = 0
    n = increase
    prepList = []
    while (i < amount):
        treeBST = None
        for x in range(1, n + 1):
            newEl = random.randint(0, 1000)
            prepList.append(newEl)
        start1 = process_time()
        for x in prepList:
            treeBST = BST.insert(treeBST, x)
        stop1 = process_time()
        start2 = process_time()
        # tworzenie drzewa AVL
        stop2 = process_time()
        timeBST = stop1 - start1
        timeAVL = stop2 - start2
        n = n + increase
        i = i + 1
    # print("time", timeBST)


def plot_graph_remove_node(amount, increase, remove):  #amount - number of repetitions, increase - more numbers, remove - how many more node/keys we are removing
    i = 0
    n = increase
    r = remove
    prepList = []
    while (i < amount):
        treeBST = None
        for x in range(1, n + 1):
            newEl = random.randint(0, 1000)
            prepList.append(newEl)
        for x in prepList:
            treeBST = BST.insert(treeBST, x)
        start1 = process_time()
        for x in prepList[:r]:
            treeBST = BST.remove(treeBST, x)
        stop1 = process_time()
        # tworzenie drzewa AVL
        start2 = process_time()
        # usuwanie z drzewa AVL
        stop2 = process_time()
        timeBST = stop1 - start1
        timeAVL = stop2 - start2
        n = n + increase
        i = i + 1
        r = r + remove
    print("time", timeBST)


def main():
    # plot_graph_create_tree(6, 800)
    plot_graph_remove_node(6, 800, 6)


if __name__ == "__main__":
    main()
