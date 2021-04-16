import matplotlib.pyplot as plt
from time import process_time
import random
import BST
from AVL import AVL_Tree, AVLNode

def plot_graph_create_tree(amount, increase):  #amount - number of repetitions, increase - how many more numbers we are adding each time to the list with random numbers
    i = 0
    n = increase
    prepList = []
    AVLprepList = []
    while (i < amount):
        treeBST = None
        treeAVL = AVL_Tree()
        rootAVL = None
        for x in range(1, n + 1):
            newEl = random.randint(0, 1000)
            prepList.append(newEl)
            AVLprepList.append(newEl)
        start1 = process_time()
        for x in prepList:
            treeBST = BST.insert(treeBST, x)
        stop1 = process_time()
        start2 = process_time()
        # tworzenie drzewa AVL
        for x in AVLprepList:
            rootAVL = treeAVL.insert(rootAVL, x)
        stop2 = process_time()
        timeBST = stop1 - start1
        timeAVL = stop2 - start2
        n = n + increase
        i = i + 1
        print("time", timeAVL)


def plot_graph_remove_node(amount, increase, remove):  #amount - number of repetitions, increase - more numbers, remove - how many more node/keys we are removing
    i = 0
    n = increase
    r = remove
    prepList = []
    AVLprepList = []
    treeAVL = AVL_Tree()
    rootAVL = None
    while (i < amount):
        treeBST = None
        for x in range(1, n + 1):
            newEl = random.randint(0, 1000)
            prepList.append(newEl)
            AVLprepList.append(newEl)
        for x in prepList:
            treeBST = BST.insert(treeBST, x)
            rootAVL = treeAVL.insert(rootAVL, x)
        start1 = process_time()
        for x in prepList[:r]:
            treeBST = BST.remove(treeBST, x)
        stop1 = process_time()
        start2 = process_time()
        # usuwanie z drzewa AVL
        for x in AVLprepList[:r]:
            rootAVL = treeAVL.delete(rootAVL, x)
        stop2 = process_time()
        timeBST = stop1 - start1
        timeAVL = stop2 - start2
        n = n + increase
        i = i + 1
        r = r + remove
        print("delete time", timeAVL)


def main():
    plot_graph_create_tree(6, 800)
    plot_graph_remove_node(6, 800, 6)


if __name__ == "__main__":
    main()
