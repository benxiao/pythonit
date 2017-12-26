BIGLEGUE = float("inf")


def minCoins(val):
    if val == 0:
        return 0
    min_v = BIGLEGUE
    for i in [1, 5, 6, 9]:
        if val - i >= 0:
            n = minCoins(val - i) + 1
            if n < min_v:
                min_v = n
    return min_v


def dp(val):
    cache = [val]*(val+1)
    coins = [1, 5, 6, 9]
    cache[0] = 0
    for j in range(1, val + 1):
        for c in coins:
            if (j - c >= 0) and (cache[j] > cache[j - c] + 1):
                    cache[j] = cache[j - c] + 1
    cur = val
    items = []
    while cur > 0:
        m = val
        for i in coins:
            if cur - i >= 0 and cache[cur - i] < m:
                m = cache[cur - i]
                c = i
        cur -= c
        items.append(c)
    return items


if __name__ == '__main__':
    # print(minCoins(81))
    print(dp(10))
