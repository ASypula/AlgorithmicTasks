class AVLNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.num = 1

    def increment(self):
        self.num += 1

    def decrement(self):
        self.num -= 1


class AVL_Tree(object):
    # recursive function
    #  1. insert key in subtree rooted with node
    #  2. return new root of subtree
    def insert(self, root, key):
        # starts like in BST tree
        if not root:
            return AVLNode(key)
        elif key == root.key:  # if node with that key exits, increment counter in node
            root.increment()
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # update height of 'root' node of the subtree
        max_child = max(self.get_height(root.left), self.get_height(root.right))
        root.height = 1 + max_child

        # calculate the balance factor
        # and rebalance tree (if needed)
        balance = self.get_balance(root)

        '''
        There are 4 different cases to rebalance tree
        It depends on nodes position before balancing

        '''
        # nodes positions: Left Left
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # nodes positions: Right Right
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        # Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        return root

    def rotate_left(self, z):

        y = z.right
        T2 = y.left

        # rotation
        y.left = z
        z.right = T2

        # update heights
        max_h = max(self.get_height(z.left), self.get_height(z.right))
        z.height = 1 + max_h
        max_h = max(self.get_height(y.left), self.get_height(y.right))
        y.height = 1 + max_h

        # return new root
        return y

    def rotate_right(self, z):

        y = z.left
        T3 = y.right

        # rotation
        y.right = z
        z.left = T3

        # update heights
        max_h = max(self.get_height(z.left), self.get_height(z.right))
        z.height = 1 + max_h
        max_h = max(self.get_height(y.left), self.get_height(y.right))
        y.height = 1 + max_h

        # return new root
        return y

    def get_height(self, root):
        if not root:
            return 0

        return root.height

    def get_balance(self, root):
        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def print_preorder(self, root):

        if not root:
            return

        print("{0} ".format(root.key), end="")
        self.print_preorder(root.left)
        self.print_preorder(root.right)

    def delete(self, root, key):
        #  delete given key from subtree with given root.
        #  returns root of the modified subtree.

        # standard BST delete
        if not root:
            return root

        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.num  > 1:
                root.num -= 1
            else:
                if root.left is None:
                    temp = root.right
                    root = None
                    return temp

                elif root.right is None:
                    temp = root.left
                    root = None
                    return temp

                temp = self.get_min(root.right)
                root.key = temp.key
                root.right = self.delete(root.right, temp.key)

        # if the tree has only one node
        # return it
        if root is None:
            return root

        # update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # calculate the balance factor
        balance = self.get_balance(root)

        # rebalance

        # Left Left
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)

        # Right Right
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)

        # Right Left
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        # Left Right
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        return root

    def get_min(self, root):
        if root is None or root.left is None:
            return root

        return self.get_min(root.left)


# myTree = AVL_Tree()
# root = None

# root = myTree.insert(root, 1)
# root = myTree.insert(root, 4)
# root = myTree.insert(root, 5)
# myTree.print_preorder(root)
