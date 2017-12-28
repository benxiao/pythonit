from binarytree import BinarySearchTree


def height(node):
    if node is None:
        return -1
    return node.height


def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1


class AVLTree(BinarySearchTree):
    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)

    def rebalance(self, node):
        while node is not None:
            update_height(node)
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent

    def insert(self, k):
        node = super().insert(k)
        self.rebalance(node)

    def remove(self, k):
        node = super().remove(k)
        self.rebalance(node)


if __name__ == '__main__':
    import random

    lst = list(range(30))
    random.shuffle(lst)
    avl = AVLTree()
    for i in lst:
        avl.insert(i)
        print(avl)
        print()
    print("-" * 50)
    print("-" * 50)

    for i in lst:
        avl.remove(i)
        print(avl)
        print()
