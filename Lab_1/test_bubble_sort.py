from bubble_sort import bubble_sort


def test_bubble_sort_words():
    text = """Śród takich pól przed laty, nad brzegiem ruczaju,
    Na pagórku niewielkim, we brzozowym gaju """
    arr = text.split()
    arr = bubble_sort(arr)
    assert arr == ['brzegiem', 'brzozowym', 'gaju', 'laty,',
                   'Na', 'nad', 'niewielkim,', 'pagórku',
                   'przed', 'pól', 'ruczaju', 'takich', 'we', 'Śród']


def test_bubble_sort_numbers():
    arr = [1, 10, 9, 5, 4, 3, 2, 7, 6, 8]
    arr = bubble_sort(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_bubble_sort_sorted():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr = bubble_sort(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_bubble_sort_repetitions():
    arr = [1, 2, 2, 7, 5, 6, 7, 10, 9, 8]
    arr = bubble_sort(arr)
    assert arr == [1, 2, 2, 5, 6, 7, 7, 8, 9, 10]
