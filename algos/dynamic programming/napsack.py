def print_tbl(tbl):
    for row in tbl:
        print(" ".join(str(x).center(9) for x in row))
    print()


# bounded napsack problem
def napsack(values, weights, limit):
    assert len(weights) == len(values)
    weights.insert(0, None)  # insert placeholder
    values.insert(0, None)  # insert placeholder
    l = len(values)
    tbl = [[0] * (limit + 1) for _ in range(l)]
    keep = [[0] * (limit + 1) for _ in range(l)]

    for i in range(1, l):
        for wi in range(limit + 1):
            leave = tbl[i - 1][wi]
            if wi >= weights[i]:
                take = tbl[i - 1][wi - weights[i]] + values[i]
                if take > leave:
                    tbl[i][wi] = take
                    keep[i][wi] = 1
                else:
                    tbl[i][wi] = leave
                    keep[i][wi] = 0
            else:
                tbl[i][wi] = leave
                keep[i][wi] = 0

    i = len(weights) - 1
    j = limit
    ids = []
    # backtracking
    while i > 0:
        if keep[i][j]:
            ids.append(i)
            j -= weights[i]
        i -= 1
    #print_tbl(tbl)
    #print_tbl(keep)
    print(ids)
    for i in ids:
        print(i, weights[i], values[i])


if __name__ == '__main__':
    import random
    random.seed(0)
    w = [random.randint(1,50) for x in range(10000)]
    v = [random.randint(1,5000) for x in range(10000)]


    napsack(v,w,300)
