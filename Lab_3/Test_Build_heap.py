from Build_heap import buildHeapInsertion, insert


def test_2_element_k2():
    arr = [3, 11]
    heap = [11, 3]
    arr = buildHeapInsertion(arr, 2)
    assert(arr == heap)


def test_2_element_k3():
    arr = [3, 11]
    heap = [11, 3]
    arr = buildHeapInsertion(arr, 3)
    assert(arr == heap)


def test_2_element_k4():
    arr = [3, 11]
    heap = [11, 3]
    arr = buildHeapInsertion(arr, 4)
    assert(arr == heap)


def test_4_element_k2():
    arr = [3, 11, 2, 20]
    heap = [20, 11, 2, 3]
    arr = buildHeapInsertion(arr, 2)
    assert(arr == heap)


def test_4_element_k3():
    arr = [3, 11, 2, 20]
    heap = [20, 3, 2, 11]
    arr = buildHeapInsertion(arr, 3)
    assert(arr == heap)


def test_4_element_k4():
    arr = [3, 11, 2, 20]
    heap = [20, 3, 2, 11]
    arr = buildHeapInsertion(arr, 4)
    assert(arr == heap)


def test_10_element_k2():
    arr = [2, 80, 17, 22, 3, 11, 2, 20, 100, 5]
    heap = [100, 80, 17, 22, 5, 11, 2, 2, 20, 3]
    arr = buildHeapInsertion(arr, 2)
    assert(arr == heap)


def test_10_element_k3():
    arr = [2, 80, 17, 22, 3, 11, 2, 20, 100, 5]
    heap = [100, 11, 80, 22, 2, 3, 2, 17, 20, 5]
    arr = buildHeapInsertion(arr, 3)
    assert(arr == heap)


def test_10_element_k4():
    arr = [2, 80, 17, 22, 3, 11, 2, 20, 100, 5]
    heap = [100, 80, 17, 22, 3, 2, 2, 11, 20, 5]
    arr = buildHeapInsertion(arr, 4)
    assert(arr == heap)


def test_insert_4th_element_k2():
    arr = [55, 21, 9]
    heap = [55, 37, 9, 21]
    insert(arr, 2, 37)
    assert(arr == heap)


def test_insert_4th_element_k3():
    arr = [55, 21, 9]
    heap = [55, 21, 9, 37]
    insert(arr, 3, 37)
    assert(arr == heap)


def test_insert_4th_element_k4():
    arr = [55, 21, 9]
    heap = [55, 21, 9, 37]
    insert(arr, 4, 37)
    assert(arr == heap)


def test_insert_10th_element_k2():
    arr = [80, 17, 22, 5, 11, 2, 20, 2, 3]
    heap = [100, 80, 22, 5, 17, 2, 20, 2, 3, 11]
    insert(arr, 2, 100)
    assert(arr == heap)


def test_insert_10th_element_k3():
    arr = [100, 80, 22, 3, 11, 2, 2, 17, 5]
    heap = [100, 80, 22, 3, 11, 2, 2, 17, 5, 20]
    insert(arr, 3, 20)
    assert(arr == heap)


def test_insert_10th_element_k4():
    arr = [100, 80, 22, 3, 11, 2, 2, 17, 5]
    heap = [100, 80, 36, 3, 11, 2, 2, 17, 5, 22]
    insert(arr, 4, 36)
    assert(arr == heap)
