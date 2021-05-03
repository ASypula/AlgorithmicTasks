def restoreDown(arr, index, k):
    # child array to store indexes of all the children of given node
    child = [None]*(k+1)

    while (True):
        # child[i]=-1 if the node is a leaf children
        for i in range(1, k+1):
            if (k * index + i) < len(arr):
                child[i] = k * index + i
            else:
                child[i] = -1

        max_child = -1
        max_child_index = None

        # finding the maximum of all the children of a given node
        for i in range(1, k+1):
            if (child[i] != -1 and (arr[child[i]] > max_child)):
                max_child_index = child[i]
                max_child = arr[child[i]]

        # leaf node
        if (max_child == -1):
            break

        # swap only if the key of max_child_index is greater than the key of node
        if (arr[index] < arr[max_child_index]):
            arr[index], arr[max_child_index] = arr[max_child_index], arr[index]
        index = max_child_index


# Function to build a heap from an array
def buildHeap(arr, k):
    # Heapify all internal nodes starting from last non-leaf node
    i = int((len(arr) - 1) / k)
    while (i >= 0):
        restoreDown(arr, i, k)
        i = i-1
