from tree import Node, in_order
import time


# w = ["A", "B", "C", "D", "E", "F", "G"]
# f = [3, 5, 1, 2, 10, 6, 5]

def printTable(x):
    for row in x:
        print(*(str(x).center(5) for x in row))
    print()


def sum_lookup(tbl_sum, i, j):
    if j < 0: return 0
    return tbl_sum[i][j]


def cost_lookup(tbl_cost, i, j):
    return tbl_cost[i][j] if j >= i else 0


def root_index_lookup(tbl_root, i, j):
    return tbl_root[i][j].value


if __name__ == '__main__':
    start = time.time()
    # w = ["A", "B", "C", "D", "E", "F", "G"]
    # f = [3, 5, 1, 2, 10, 6, 5]
    items = []
    with open("calcfreq2.txt") as fp:
        for line in fp:
            w, f = line.rstrip().split()
            f = int(f)
            items.append((w, f))
    print("uploaded the file")
    w = [w for w, _ in items]
    f = [f for _, f in items]
    l = len(w)
    MAX_COST = 2 ** 32

    tbl_cost = [[0] * l for _ in range(l)]
    tbl_sum = [[0] * l for _ in range(l)]
    tbl_root = [[None] * l for _ in range(l)]
    print("finsh creating three tables")

    for i in range(l):
        for j in range(i, l):
            tbl_sum[i][j] += sum_lookup(tbl_sum, i, j - 1) + f[j]

    print("finish sum table")

    for i in range(l):
        tbl_cost[i][i] = f[i]
        tbl_root[i][i] = Node(w[i], i, f[i])

    print("finish node table")
    # printTable(tbl_cost)
    for k in range(1, l):
        i = -1
        for j in range(k, l):
            i += 1
            tbl_cost[i][j] = MAX_COST
            min_r = None
            print(i, j)
            left = root_index_lookup(tbl_root, i, j - 1)  # r index for left
            down = root_index_lookup(tbl_root, i + 1, j)  # r index for down
            # print("name", tbl_root[i][j-1].key, "value", left)
            for m in range(left, down+1):
                cost = sum([cost_lookup(tbl_cost, i, m - 1),
                            cost_lookup(tbl_cost, m + 1, j),
                            sum_lookup(tbl_sum, i, j)])
                if cost < tbl_cost[i][j]:
                    tbl_cost[i][j] = cost
                    min_r = m

            new_root = Node(w[min_r], min_r, f[min_r])
            tbl_root[i][j] = new_root
            if min_r - 1 >= i:
                left_root = tbl_root[i][min_r - 1]
                new_root.add_left(left_root)

            if min_r + 1 <= j:
                right_root = tbl_root[min_r + 1][j]
                new_root.add_right(right_root)

                # printTable(tbl_cost)

    m_tree = tbl_root[0][l - 1]
    assert m_tree.check_invariant()
    # print(m_tree.ascii_art())
    # printTable(tbl_cost)
    total = tbl_sum[0][l-1]
    lst = []
    in_order(lst, m_tree, 1)
    cumsum = 0

    with open("mincostbst_essay.txt", "w") as outfp:
        for node, level in lst:
            cumsum += node.freq * level / total
            print("".join(str(x).center(15) for x in[node.key, node.freq, level,
                          round(cumsum, 6)]), file=outfp)

    print(time.time() - start)
