from merge_sort import merge_sort


def test_merge_sort_words():
    text = """Śród takich pól przed laty, nad brzegiem ruczaju, na pagórku niewielkim, we brzozowym gaju """
    arr = text.split()
    arr = merge_sort(arr)
    assert arr == ['brzegiem', 'brzozowym', 'gaju', 'laty,',
                   'na', 'nad', 'niewielkim,', 'pagórku',
                   'przed', 'pól', 'ruczaju,', 'takich', 'we', 'Śród']



def test_merge_sort_numbers():
    arr = [1, 10, 9, 5, 4, 3, 2, 7, 6, 8]
    arr = merge_sort(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_merge_sort_sorted():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr = merge_sort(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_merge_sort_with_repetitions():
    arr = [1, 2, 2, 7, 5, 6, 7, 10, 9, 8]
    arr = merge_sort(arr)
    assert arr == [1, 2, 2, 5, 6, 7, 7, 8, 9, 10]
