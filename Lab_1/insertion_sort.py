# sortowanie przez wstawianie, zlozonosc czasowa O(n^2)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        value = arr[i]
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j+1] = value
    return arr
