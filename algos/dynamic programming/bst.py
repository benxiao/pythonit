class Node:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.left=None
        self.right=None
        self.parent=None

    def add(self, node):
        if node.key < self.key:
            if not self.left:
                self.left=node
                node.parent = self
            else: self.left.add(node)
        else:
            if not self.right:
                self.right=node
                node.parent = self
            else: self.right.add(node)

    def min(self):
        cur = self
        while cur.left:
            cur = cur.left
        return cur

    def next(self):
        if self.right:
            return self.right.min()
        cur = self
        while cur.parent:
            if cur.parent.left is cur: break
            cur = cur.parent
        return cur.parent

    def prev(self):
        if self.left:
            return self.left.max()
        cur = self
        while cur.parent:
            if cur.parent.right is cur: break
            cur = cur.parent
        return cur.parent

    def find(self, key):
        if self.key > key:
            if self.left:
                return self.left.find(key)
        elif self.key < key.key:
            if self.right:
                return self.right.find(key)
        else:
            return self

    def detach(self):
        # no children
        if not self.left and not self.right:
            if self.parent.left is self:
                self.parent.left = None
                self.parent = None
            else:
                self.parent.right = None
                self.parent = None

        # two children
        if self.left and self.right:


        # one child
        if self.left or self.right:
            if self.parent.left is self:
                if self.left:
                    self.parent.left = self.left
                else:
                    self.parent.right = self.right
                self.parent.right = self.right
                self.parent = None



    def _str(self):
        """Internal method for ASCII art. credit to MIT"""
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
                [left_line + ' ' * (
                    width - left_width - right_width) + right_line
                 for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width

    def ascii_art(self):
        return '\n'.join(self._str()[0])

    def __str__(self):
        return "key: {}, value: {}".format(self.key, self.value)


if __name__ == '__main__':
    tree = Node(20, 20)
    tree.add(Node(8,8))
    tree.add(Node(22,22))
    tree.add(Node(4,4))
    tree.add(Node(12,12))
    tree.add(Node(10,10))
    tree.add(Node(14,14))
    print(tree.ascii_art())
    cur = tree.min()
    print(cur)
    while 1:
        next_node = cur.next()
        if not next_node:
            break
        print(next_node)
        cur = next_node





