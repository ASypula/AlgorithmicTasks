def restoreUp(arr, index, k):
    # parent stores the index of the parent variable of the node
    parent = int((index-1)/k)

    while parent >= 0:
        if (arr[index] > arr[parent]):
            arr[index], arr[parent] = arr[parent], arr[index]
            index = parent
            parent = int((index - 1)/k)
        else:
            break


def insert(arr, k, elem):
    arr.append(elem)
    restoreUp(arr, len(arr)-1, k)


def buildHeapInsertion(arr, k):
    heap = []
    for x in arr:
        insert(heap, k, x)
    return heap

