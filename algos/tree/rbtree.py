from binarytree import BinarySearchTree, Node

"""
A more relaxed balanced binary search tree


Invariants
Every node has a color either red or black
Root of tree is always black
There are no two adjacent red nodes(A red node cannot have a red parent or red child)
Every path from root to a NULL node has same number of black nodes.
"""

"""
if None, it is Black
if it is only red, if the node exists and node.red is True
"""


def red(node):
    return bool(node) and node.red


class RBTree(BinarySearchTree):
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

        # red black tree specific
        y.red = False
        x.red = True

    # rbtree specific
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
        y.red = False
        x.red = True

    # rbtree specific
    def rebalance(self, node):
        while node and node != self.root and node.red and node.parent.red:
            _grandparent = node.grandparent()
            _uncle = node.uncle()
            # recolor
            if red(_uncle):
                node.parent.red = False
                _uncle.red = False
                _grandparent.red = True
                node = node.grandparent()

            # rotate
            else:
                if node.parent is _grandparent.left:
                    if node is node.parent.left:
                        self.right_rotate(_grandparent)
                    else:
                        self.left_rotate(node.parent)
                        self.right_rotate(_grandparent)
                else:
                    if node is node.parent.right:
                        self.left_rotate(_grandparent)
                    else:
                        self.right_rotate(node.parent)
                        self.left_rotate(_grandparent)
                node = node.parent
        if self.root:
            self.root.red = False

    def insert(self, k):
        node = super().insert(k)
        node.red = True
        self.rebalance(node)

    def remove(self, k):
        node = super().remove(k)
        self.rebalance(node)


if __name__ == '__main__':
    import random

    lst = list(range(20))
    random.shuffle(lst)
    avl = RBTree()
    for i in lst:
        avl.insert(i)
        print(avl)
        print()
    #
    # for i in lst:
    #     avl.remove(i)
    #     print(avl)
    #     print()
