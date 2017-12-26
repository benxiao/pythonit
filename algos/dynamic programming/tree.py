class Node:
    __slots__ = ["key", "value", "freq", "left", "right", "parent"]

    def __init__(self, key, value, freq, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.freq = freq
        self.left = left
        self.right = right
        self.parent = parent

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

    def add_left(self, node):
        self.left = node
        node.parent = self

    def add_right(self, node):
        self.right = node
        node.parent = self

    def __str__(self):
        return str(self.key) #+ " " + str(self.value)

    def ascii_art(self):
        return '\n'.join(self._str()[0])

    def check_invariant(self):
        invariant = True
        left, right = None, None
        if self.left:
            if self.left.key > self.key:
                invariant = False
                left = self.left.check_invariant()
        if self.right:
            if self.right.key < self.key:
                invariant = False
                right = self.right.check_invariant()
        return all(filter(lambda x: x is not None, [invariant, left, right]))



def in_order(lst, root, level):
    if root.left:
        in_order(lst, root.left, level+1)
    lst.append((root, level))
    if root.right:
        in_order(lst, root.right, level+1)


def depth(node):
    if not node: return 0
    return 1 + max(depth(node.left), depth(node.right))


def sum_cost(node, level):
    val = node.freq * level
    if node.left:
        val += sum_cost(node.left, level + 1)
    if node.right:
        val += sum_cost(node.right, level + 1)
    return val


if __name__ == '__main__':
    root0 = Node("B", 1, 1)
    root0.add_left(Node("C", 2, 1))
    root0.add_right(Node("A", 1, 1))
    print(root0)
    root1 = root0.copy()
    print(root1)
    print(root1.check_invariant())
