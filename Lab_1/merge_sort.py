# Sortowanie przez scalanie, zlozonosc czasowa O(n*logn)

def merge_sort(arr):
    if len(arr) > 1:
        # find middle point
        middle = len(arr)//2
        # divide arr
        left_arr = arr[:middle]
        right_arr = arr[middle:]
        # sort halves
        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0
        # merge
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # check if any elements are left
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr


#list = [5, 8, 10, 1, 2, 3]
#list = merge_sort(list)
#print(list)
