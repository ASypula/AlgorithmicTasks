# sortowanie przez wybieranie, zlozonosc czasowa O(n^2)

def selection_sort(arr):
    for i in range(0, len(arr)-1):
        min_idx = i
        j = i + 1
        while j < len(arr):
            min_value = arr[min_idx]
            if arr[j] < min_value:
                min_idx = j
            j = j + 1
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr
