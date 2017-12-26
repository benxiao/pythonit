import time


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


def in_order(lst, root, level):
    if root.left:
        in_order(lst, root.left, level + 1)
    lst.append((root, level))
    if root.right:
        in_order(lst, root.right, level + 1)


def print_table(x):
    for row in x:
        print(*(str(x).center(5) for x in row))
    print()


def construct_tree(root_tbl, w, f, i, j):
    if i > j: return None
    k = root_tbl[i][j]
    node = Node(w[k], f[k])
    node.left = construct_tree(root_tbl, w, f, i, k - 1)
    node.right = construct_tree(root_tbl, w, f, k + 1, j)
    return node


if __name__ == '__main__':
    start = time.time()
    items = []
    with open("calcfreq_shakespeare.txt") as fp:
        for line in fp:
            w, f = line.rstrip().split()
            f = int(f)
            items.append((w, f))
    print("uploaded the file")

    w = [w for w, _ in items]
    f = [f for _, f in items]
    l = len(w)
    MAX_COST = float("inf")

    tbl_cost = [[0] * l for _ in range(l)]
    tbl_sum = [[0] * l for _ in range(l)]
    tbl_root = [[0] * l for _ in range(l)]
    print("finsh creating three tables")

    for i in range(l):
        for j in range(i, l):
            tbl_sum[i][j] = tbl_sum[i][j - 1] + f[j]
    print("finish sum table")

    for i in range(l):
        tbl_cost[i][i] = f[i]
        tbl_root[i][i] = i
    print("finish node table")

    for k in range(1, l):
        i = -1
        for j in range(k, l):
            i += 1
            tbl_cost[i][j] = MAX_COST
            min_r = None
            #print(i, j) # used for debug, but will kill performance
            left = tbl_root[i][j - 1] # left bound
            down = tbl_root[i + 1][j] # down bound
            for m in range(left, down + 1):
                left_subtree = tbl_cost[i][m - 1] if m - 1 >= i else 0
                right_subtree = tbl_cost[m + 1][j] if m + 1 <= j else 0
                cost = left_subtree + right_subtree + tbl_sum[i][j]
                if cost < tbl_cost[i][j]:
                    tbl_cost[i][j] = cost
                    min_r = m
            tbl_root[i][j] = min_r

    m_tree = construct_tree(tbl_root, w, f, 0, l - 1)
    lst = []
    in_order(lst, m_tree, 1)
    cumsum = 0
    total = tbl_sum[0][l - 1]
    with open("mincostbst_essay.txt", "r") as outfp:
        for node, level in lst:
            cumsum += node.value * level / total
            print("".join(str(x).center(15) for x in [node.key, node.value,
                                                    level, round(cumsum, 6)]),
                file=None)
    print(time.time() - start)
