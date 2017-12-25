n_calls = 0


def comb(n, m):
    global n_calls
    n_calls += 1
    print("comb({}, {})".format(n, m))
    if n == 0 or m == 0 or n == m:
        return 1
    return comb(n - 1, m) + comb(n - 1, m - 1)


weights = [3, 4, 7, 8, 9]
values = [4, 5, 10, 11, 13]
cap = 17


# top down approach
def knapsack(weights, values, cap, cache):
    if cap in cache:
        return cache[cap]
    else:

        results = []
        for w, v in zip(weights, values):
            if cap >= w:
                result = knapsack(weights, values, cap - w, cache) + v
                results.append(result)
        if not results:
            cache[cap] = 0
            return 0

        largest = max(results)
        cache[cap] = largest
        return largest


# bottom up approach


# rod cutting problem






if __name__ == '__main__':
    # print(comb(10, 4))
    # print(n_calls)

    print(knapsack(weights, values, 17, {}))
