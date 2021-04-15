class Node:
    def __init__(self, key):
        self.key = key
        self.number = 1
        self.left = None
        self.right = None

    def increment(self):
        self.number = self.number + 1

    def decrement(self):
        self.number = self.number - 1


def tree_list(root, tree):
    if root is not None:
        tree_list(root.left, tree)
        tree.append(root.key)
        tree_list(root.right, tree)
    return tree


def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif (key == node.key):
        node.increment()
    else:
        node.right = insert(node.right, key)
    return node


def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current


def remove(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = remove(root.left, key)
    elif(key > root.key):
        root.right = remove(root.right, key)
    else:
        if root.number > 1:
            root.decrement()
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = minValueNode(root.right)
            root.key = temp.key
            root.right = remove(root.right, temp.key)
    return root

