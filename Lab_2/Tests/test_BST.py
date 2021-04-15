import BST


def test_create_BST1():
    z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    treeList = []
    tree = None
    for x in z:
        tree = BST.insert(tree, x)
    treeList = BST.tree_list(tree, treeList)
    assert z == treeList


def test_create_BST2():
    z = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    correct = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    treeList = []
    tree = None
    for x in z:
        tree = BST.insert(tree, x)
    treeList = BST.tree_list(tree, treeList)
    assert correct == treeList


def test_create_BST3():
    z = [85, 7, 49, 25, 66, 93, 70, 67, 24, 83, 6, 77, 35, 53, 44, 85, 7, 64, 58, 82]
    correct = [6, 7, 24, 25, 35, 44, 49, 53, 58, 64, 66, 67, 70, 77, 82, 83, 85, 93]
    treeList = []
    tree = None
    for x in z:
        tree = BST.insert(tree, x)
    treeList = BST.tree_list(tree, treeList)
    assert correct == treeList


def test_create_BST4():
    z = [10, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    correct = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    treeList = []
    tree = None
    for x in z:
        tree = BST.insert(tree, x)
    treeList = BST.tree_list(tree, treeList)
    assert correct == treeList


def test_remove_BST1():
    z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    treeList = []
    tree = None
    for x in z:
        tree = BST.insert(tree, x)
    tree = BST.remove(tree, 1)
    treeList = BST.tree_list(tree, treeList)
    correct = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert correct == treeList


def test_remove_BST2():
    z = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    treeList = []
    tree = None
    for x in z:
        tree = BST.insert(tree, x)
    tree = BST.remove(tree, 2)
    treeList = BST.tree_list(tree, treeList)
    correct = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert correct == treeList


def test_remove_BST3():
    z = [81, 91, 73, 22, 26, 24, 34, 59, 44, 20, 84, 6, 11, 23, 52, 7, 5, 58, 2, 95]
    treeList = []
    tree = None
    for x in z:
        tree = BST.insert(tree, x)
    for i in range(0, 3):
        tree = BST.remove(tree, z[i])
    treeList = BST.tree_list(tree, treeList)
    correct = [2, 5, 6, 7, 11, 20, 22, 23, 24, 26, 34, 44, 52, 58, 59, 84, 95]
    assert correct == treeList
