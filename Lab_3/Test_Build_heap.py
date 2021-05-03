from Build_heap import buildHeap


def test_2_element_k2():
    arr = [3, 11]
    heap = [11, 3]
    buildHeap(arr, 2)
    assert(arr == heap)


def test_2_element_k3():
    arr = [3, 11]
    heap = [11, 3]
    buildHeap(arr, 3)
    assert(arr == heap)


def test_2_element_k4():
    arr = [3, 11]
    heap = [11, 3]
    buildHeap(arr, 4)
    assert(arr == heap)


def test_4_element_k2():
    arr = [3, 11, 2, 20]
    heap = [20, 11, 2, 3]
    buildHeap(arr, 2)
    assert(arr == heap)


def test_4_element_k3():
    arr = [3, 11, 2, 20]
    heap = [20, 11, 2, 3]
    buildHeap(arr, 3)
    assert(arr == heap)


def test_4_element_k4():
    arr = [3, 11, 2, 20]
    heap = [20, 11, 2, 3]
    buildHeap(arr, 4)
    assert(arr == heap)


def test_10_element_k2():
    arr = [2, 80, 17, 22, 3, 11, 2, 20, 100, 5]
    heap = [100, 80, 17, 22, 5, 11, 2, 20, 2, 3]
    buildHeap(arr, 2)
    assert(arr == heap)


def test_10_element_k3():
    arr = [2, 80, 17, 22, 3, 11, 2, 20, 100, 5]
    heap = [100, 80, 20, 22, 3, 11, 2, 2, 17, 5]
    buildHeap(arr, 3)
    assert(arr == heap)


def test_10_element_k4():
    arr = [2, 80, 17, 22, 3, 11, 2, 20, 100, 5]
    heap = [100, 80, 17, 22, 3, 11, 2, 20, 2, 5]
    buildHeap(arr, 4)
    assert(arr == heap)
