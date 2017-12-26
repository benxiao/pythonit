from tree import Node, output
import operator
import time


# w = ["A", "B", "C", "D", "E", "F", "G"]
# f = [3,    5,   1,   2,   10,  6,   5]

items = []
with open("frequencies.txt") as fp:
    for line in fp:
        w, f = line.rstrip().split()
        f = int(f)
        items.append((w, f))

items.sort(key=operator.itemgetter(0))
w = [w for w, _ in items]
f = [f for _, f in items]
l = len(w)
MAX_COST = 2 ** 32


def printTable(x):
    for row in x:
        print(*(str(x).center(5) for x in row))
    print()


def sum_lookup(tbl_sum, i, j):
    return tbl_sum[i][j]


def cost_lookup(tbl_cost, i, j):
    return tbl_cost[i][j] if j >= i else 0


if __name__ == '__main__':
    start = time.time()
    items = []
    # with open("frequencies.txt") as fp:
    #     for line in fp:
    #         w, f = line.rstrip().split()
    #         f = int(f)
    #         items.append((w, f))
    # print("uploaded the file")
    # items.sort(key=operator.itemgetter(0))
    # w = [w for w, _ in items]
    # f = [f for _, f in items]
    l = len(w)
    MAX_COST = 2 ** 32


    tbl_cost = [[0] * l for _ in range(l)]
    tbl_sum = [[0] * l for _ in range(l)]
    tbl_root = [[None] * l for _ in range(l)]

    # for i in range(l):
    #     for j in range(i, l):
    #         tbl_sum[i][j] = sum(f[i:j + 1])
    # # print(tbl_sum)

    for i in range(l):
        for j in range(i, l):
            tbl_sum[i][j] += sum_lookup(tbl_sum, i, j - 1) + f[j]

    for i in range(l):
        tbl_cost[i][i] = f[i]
        tbl_root[i][i] = Node(w[i],i, f[i])

    # printTable(tbl_root)

    # printTable(tbl_cost)
    n = l - 1
    j = 1

    while n >= 0:  # n
        for i in range(n):  # n
            tbl_cost[i][i + j] = MAX_COST
            min_r = None

            for r in range(i, i + j + 1):
                """
                OBST(i,r-1) + OBST(r+1, j) + sum(i,j)
                """
                cost = cost_lookup(tbl_cost, i, r - 1) \
                       + cost_lookup(tbl_cost, r + 1, j + i) \
                       + sum_lookup(tbl_sum, i, j + i)
                # print(i, r,  j + i, sum_lookup(tbl_sum, i, j + i), cost)
                if cost < tbl_cost[i][i + j]:
                    tbl_cost[i][i + j] = cost
                    min_r = r

            new_root = Node(w[min_r], min_r, f[min_r])
            tbl_root[i][i + j] = new_root
            if min_r-1 >= i:
                left_root = tbl_root[i][min_r-1]
                new_root.add_left(left_root)
            if min_r+1 <= i+j:
                right_root = tbl_root[min_r+1][i+j]
                new_root.add_right(right_root)
        j += 1
        n -= 1


#print(tbl_root[0][l-1])
root = tbl_root[0][l-1]
#print(root.ascii_art())
#print(tbl_cost[0][l-1])
output(root, None)
#printTable(tbl_cost)
#printTable(tbl_root)
#printTable(tbl_root)
print(time.time()-start)

