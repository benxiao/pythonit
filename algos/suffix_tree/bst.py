class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.height = 0
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, node):
        if node.key < self.key:
            if not self.left:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        else:
            if not self.right:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)

    def find(self, key):
        if key == self.key:
            return self
        if key < self.key:
            if self.left:
                return self.left.find(key)
        else:
            if self.right:
                return self.right.find(key)

    def min(self):
        if not self.left:
            return self
        return self.left.min()

    def max(self):
        if not self.right:
            return self
        return self.right.max()

    def next_larger(self):
        if self.right:
            return self.right.min()
        cur = self
        while cur.parent:
            if cur.parent.left is cur:
                break
            cur = cur.parent
        return cur.parent

    def _str(self):
        """Internal method for ASCII art."""
        label = str(self.key)
        if self.left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            left_lines, left_pos, left_width = self.left._str()
        if self.right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self.right._str()
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and self.parent is not None and \
                        self is self.parent.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.': label = ' ' + label[1:]
        if label[-1] == '.': label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle - 2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
                [left_line + ' ' * (width - left_width - right_width) + right_line
                 for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width

    def ascii(self):
        return '\n'.join(self._str()[0])

    def __str__(self):
        return str(self.key)

    def deleted(self):
        if (not self.left) or (not self.right):
            if self.parent.left is self:
                self.parent.left = self.left or self.right
                if self.parent.left:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right:
                    self.parent.right.parent = self.parent
            return self
        else:
            successor = self.next_larger()
            self.key, successor.key = successor.key, self.key
            self.val, successor.val = successor.val, self.val
            return successor.deleted()


class AVLTree:
    def __init__(self):
        self.root = None
        self.sz = 0

    @staticmethod
    def set_height(node):
        left_height = node.left.height if node.left else -1
        right_height = node.right.height if node.right else -1
        node.height = max(left_height, right_height) + 1

    @staticmethod
    def get_height(node):
        return node.height if node else -1

    def insert(self, key, val):
        new_node = Node(key, val)
        if not self.root:
            self.root = new_node
            self.sz = 1
            return
        node = self.root.find(key)
        if not node:
            self.root.insert(new_node)
            self._balance(new_node)
            self.sz += 1
        else:
            node.val = val

    def __contains__(self, key):
        return self.root.find(key) is not None

    def __getitem__(self, key):
        node = self.root.find(key)
        if node:
            return node.val

    def next_larger(self, key):
        node = self.root.find(key)
        if node:
            next_node = node.next_larger()
            if next_node:
                return (next_node.key, next_node.val)

    def min(self):
        return self.root.min() if self.root else None

    def _balance(self, node):
        cur = node
        while cur:
            self.set_height(cur)
            left_child_height = self.get_height(cur.left)
            right_child_height = self.get_height(cur.right)
            if left_child_height > right_child_height + 1:
                child = cur.left
                if self.get_height(child.left) > self.get_height(child.right):
                    print("rotate_right")
                    self._right_rotate(cur)
                    print("new cur: ", cur)
                    print("new cur's parent: ", cur.parent)
                else:
                    print("rotate_left_then_right")
                    self._left_rotate(child)
                    self._right_rotate(cur)

            elif left_child_height + 1 < right_child_height:
                child = cur.right
                if self.get_height(child.left) < self.get_height(child.right):
                    print("rotate_left")
                    self._left_rotate(cur)
                else:
                    print("rotate_right_then_left")
                    self._right_rotate(child)
                    self._left_rotate(cur)
            cur = cur.parent

    def _left_rotate(self, node):
        a = node
        b = node.right
        a.right = b.left
        if b.left: a.right.parent = a
        if a.parent:
            if a.parent.left is a:
                a.parent.left = b
                b.parent = a.parent
            else:
                a.parent.right = b
                b.parent = a.parent
        else:
            b.parent = None
        b.left = a
        a.parent = b
        AVLTree.set_height(a)
        AVLTree.set_height(b)
        if a is self.root:
            self.root = b

    def _right_rotate(self, node):
        b = node
        a = node.left
        b.left = a.right
        if a.right: b.left.parent = b
        if b.parent:
            if b.parent.left is b:
                b.parent.left = a
                a.parent = b.parent
            else:
                b.parent.right = a
                a.parent = b.parent
        else:
            a.parent = None
        a.right = b
        b.parent = a
        AVLTree.set_height(b)
        AVLTree.set_height(a)
        if b is self.root:
            self.root = a

    def delete(self, key):
        node = self.root.find(key)
        if not node:
            raise KeyError()
        deleted_node = node.deleted()
        self._balance(deleted_node.parent)
        return deleted_node

    def __str__(self):
        if self.root:
            return self.root.ascii()
        else:
            return "<emtpy tree>"


if __name__ == '__main__':
    import random

    lst = list(range(64))
    random.shuffle(lst)
    tree = AVLTree()

    for i in lst:
        print("insert key:", i)
        tree.insert(i, i)
    # print(tree)
    #
    # for i in lst[:118]:
    #     tree.delete(i)
    #     print(tree)
    print(tree)