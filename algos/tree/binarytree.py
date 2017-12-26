class Node:
    def __init__(self, k, left=None, right=None, parent=None):
        self.key = k
        self.left = left
        self.right = right
        self.parent = parent

    def find(self, k):
        if k == self.key:
            return self
        elif k < self.key and self.left:
            return self.left.find(k)
        elif k > self.key and self.right:
            return self.right.find(k)
        else:
            return None

    def min(self):
        if self.left:
            return self.left.min()
        return self

    def max(self):
        if self.right:
            return self.right.max()
        return self

    def next(self):
        if self.right:
            return self.right.min()
        cur = self.parent
        while cur and cur.parent.right is cur:
            cur = cur.parent
        return cur.parent

    def insert(self, k):
        _node = Node(k)
        if k < self.key:
            if self.left:
                return self.left.insert(k)
            else:
                self.left = _node
                _node.parent = self
        else:
            if self.right:
                return self.right.insert(k)
            else:
                self.right = _node
                _node.parent = self
        return _node

    def delete(self):
        if self.left and self.right:
            sub = self.right.min()
            self.key = sub.k
            sub.delete()

        elif self.parent.left is self:
            self.parent.left = self.right or self.left
            if self.parent.left:
                self.parent.left.parent = self.parent

        elif self.parent.right is self:
            self.parent.right = self.right or self.left
            if self.parent.right:
                self.parent.right.parent = self.parent

    def remove(self, k):
        found = self.find(k)
        if not found:
            return
        return found.delete()

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

    def __str__(self):
        return "\n".join(self._str()[0])


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.n = 0

    def insert(self, k):
        if self.root is None:
            self.root = Node(k)
        else:
            self.root.insert(k)
        self.n += 1

    def __contains__(self, k):
        if self.root is None:
            return False
        return self.root.find(k) is not None

    def __str__(self):
        return str(self.root) if self.root else "<empty>"

    def remove(self, k):
        if not self.root:
            return

        _node = self.root.find(k)
        if not _node:
            return

        if _node is self.root:
            if self.root.right:
                sub = self.root.right.min()
                self.root.key = sub.key
                sub.delete()
            else:
                self.root = self.root.left
                if self.root:
                    self.root.parent = None
        else:
            _node.delete()


if __name__ == '__main__':
    tree = BinarySearchTree()
    for i in [9, 1, 3, 4, 6, 2]:
        tree.insert(i)

    print(tree.root)
    for i in [9, 1, 3, 4, 6, 2]:
        tree.remove(i)
        print(tree)
        print()
