from tree import Node, print_preorder, sum_cost
from bisect import bisect_right
import operator
import time

# w = ["A", "B", "C", "D", "E", "F", "G"]
# f = [3, 5, 1, 2, 10, 6, 5]


def find_balance(cumsum, t, l, h):
    ri = bisect_right(cumsum, t, l, h)
    li = ri - 1
    if li >= l:
        if abs(cumsum[ri] - t) > abs(cumsum[li] - t):
            ri = li
    return ri


def construct_tree(cumsum, l, h):
    if h - l < 1:
        return

    if h - l == 1:
        return Node(w[l], 0, f[l])

    t = (cumsum[l] + cumsum[h - 1]) // 2
    mid = find_balance(cumsum, t, l, h)
    root = Node(w[mid], 0, f[mid])
    left_sub = construct_tree(cumsum, l, mid)
    if left_sub:
        root.add_left(left_sub)

    right_sub = construct_tree(cumsum, mid + 1, h)
    if right_sub:
        root.add_right(right_sub)

    return root


if __name__ == '__main__':
    start = time.time()
    items =[]
    with open("frequencies.txt") as fp:
        for line in fp:
            w, f = line.rstrip().split()
            f = int(f)
            items.append((w, f))
    print("uploaded the file")
    items.sort(key=operator.itemgetter(0))
    w = [w for w, _ in items]
    f = [f for _, f in items]

    cumsum = f[:]
    l = len(cumsum)
    for i in range(1, len(cumsum)):
        cumsum[i] += cumsum[i - 1]

    root = construct_tree(cumsum, 0, len(cumsum))
    print_preorder(root, 0, None)
    print(sum_cost(root, 1))
    print(time.time()-start)