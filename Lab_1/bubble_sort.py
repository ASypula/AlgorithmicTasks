# Sortowanie babelkowe, zlozonosc czasowa O(n^2)

def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        ordered = True
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                # swap elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                ordered = False
        if ordered:
            break
    return arr


# list = [5, 8, 10, 1, 2, 3]
# list = bubbleSort(list)
# print(list)
