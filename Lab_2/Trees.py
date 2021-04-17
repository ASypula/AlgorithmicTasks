import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt_delete
from time import process_time
import random
import BST
from AVL import AVL_Tree, AVLNode

def plot_graph_create_tree(amount, increase):  #amount - number of repetitions, increase - how many more numbers we are adding each time to the list with random numbers
    i = 0
    n = increase
    prepList = []
    AVLprepList = []
    # keys[], values[] are used later to create chart
    keysBST = []
    valuesBST = []
    keysAVL = []
    valuesAVL = []
    # results[] store results that will be added to file
    results_AVL = []
    results_BST = []
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
        results_BST.append(f'inserted {n} elements to BST tree time: {timeBST}')
        print(f'inserted {n} elements to BST tree, time: {timeBST}')
        results_AVL.append(f'inserted {n} element to AVL tree, time: {timeAVL}')
        print(f'inserted {n} elements to AVL tree, time: {timeAVL}')
        keysBST.append(n)
        valuesBST.append(timeBST)
        keysAVL.append(n)
        valuesAVL.append(timeAVL)
        n = n + increase
        i = i + 1

    plt.plot(keysBST, valuesBST, label="BST")
    plt.plot(keysAVL, valuesAVL, label="AVL")
    plt.title(label="Insertion times")
    plt.xlabel("n")
    plt.ylabel("t [s]")
    plt.axis([0, 11000, 0, 2.5])
    plt.legend()

    plt.savefig("Insertion_times.png")
    plt.show()
    plt.clf()
    with open ("wyniki_AVL.txt", 'w') as fh:
        for line in results_AVL:
            fh.write(line)
            fh.write('\n')

    with open ("wyniki_BST.txt", 'w') as fh:
            for line in results_BST:
                fh.write(line)
                fh.write('\n')



def plot_graph_remove_node(amount, increase, remove):  #amount - number of repetitions, increase - more numbers, remove - how many more node/keys we are removing
    i = 0
    n = increase
    r = remove
    prepList = []
    AVLprepList = []
    treeAVL = AVL_Tree()
    rootAVL = None
    keysBST = []
    valuesBST = []
    keysAVL = []
    valuesAVL = []
    results_AVL = []
    results_BST = []
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
        results_BST.append(f'deleted {r} elements from BST tree, time: {timeBST}')
        print(f'deleted {r} elements from BST tree, time: {timeBST}')
        results_AVL.append(f'deleted {r} elements from AVL tree, time: {timeAVL}')
        print(f'deleted {r} elements from AVL tree, time: {timeAVL}')
        keysBST.append(r)
        valuesBST.append(timeBST)
        keysAVL.append(r)
        valuesAVL.append(timeAVL)
        n = n + increase
        i = i + 1
        r = r + remove
        print("delete time", timeAVL)
    plt.plot(keysBST, valuesBST, label="BST")
    plt.plot(keysAVL, valuesAVL, label="AVL")
    plt.title(label="Delete times")
    plt.xlabel('n')
    plt.ylabel("t [s]")
    plt.axis([100, 1500, 0, 0.05])
    plt.savefig("Delete_times.png")
    plt.show()
    plt.clf()

    with open ("wyniki_AVL.txt", 'a') as fh:
        for line in results_AVL:
            fh.write(line)
            fh.write('\n')

    with open ("wyniki_BST.txt", 'a') as fh:
            for line in results_BST:
                fh.write(line)
                fh.write('\n')


def main():
    plot_graph_create_tree(20, 500)
    print('\n\n')
    plot_graph_remove_node(30, 100, 50)


if __name__ == "__main__":
    main()
