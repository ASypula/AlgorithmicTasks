from AVL import AVL_Tree,AVLNode

def test_insert_typical():
    num = [1, 4, 5]
    tree = AVL_Tree()
    root = None
    for number in num:
        root = tree.insert(root, number)
    tree.preorder(root)
    assert tree.list_preorder == [4, 1, 5]


def test_insert_typical_2():
    num = [14, 17, 11, 7, 53, 4, 13]
    tree = AVL_Tree()
    root = None
    for number in num:
        root = tree.insert(root, number)
    tree.preorder(root)
    assert tree.list_preorder == [14, 7, 4, 11, 13, 17, 53]


def test_insert_with_rep():
    num = [1, 1, 4, 5, 5, 4]
    tree = AVL_Tree()
    root = None
    for number in num:
        root = tree.insert(root, number)
    tree.preorder(root)
    assert tree.list_preorder == [4, 1, 5]




def test_delete_typical():
    num = [1, 4, 5]
    tree = AVL_Tree()
    root = None
    for number in num:
        root = tree.insert(root, number)
    tree.preorder(root)
    assert tree.list_preorder == [4, 1, 5]
    tree.list_preorder = []
    root = tree.delete(root, 5)
    tree.preorder(root)
    assert tree.list_preorder == [4, 1]


def test_delete_all():
    num = [14, 17, 11, 7, 53, 4, 13]
    tree = AVL_Tree()
    root = None
    for number in num:
        root = tree.insert(root, number)
    for number in num:
        root = tree.delete(root, number)
    tree.preorder(root)
    assert tree.list_preorder == []


def test_delete_with_rep():
    num = [1, 4, 5, 5]
    tree = AVL_Tree()
    root = None
    for number in num:
        root = tree.insert(root, number)
    tree.preorder(root)
    assert tree.list_preorder == [4, 1, 5]
    tree.list_preorder = []
    root = tree.delete(root, 5)
    tree.preorder(root)
    assert tree.list_preorder == [4, 1, 5]
    tree.list_preorder = []
    root = tree.delete(root, 5)
    tree.preorder(root)
    assert tree.list_preorder == [4, 1]
