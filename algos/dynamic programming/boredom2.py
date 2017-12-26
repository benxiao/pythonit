from collections import Counter

a = [1, 2, 1, 3, 2, 2, 2, 2, 3]
c = Counter(a)
print(c)


def boredom(d, memo):
    try:
        return memo[str(d)]
    except KeyError:
        if not d:
            memo[str(d)] = 0
            return 0
        max_points = 0
        for i, n in enumerate(d):
            next_d = Counter(d)
            if next_d[n] > 1:
                next_d[n] -= 1
            else:
                next_d.pop(n)
            if n+1 in next_d:
                next_d.pop(n+1)

            if n-1 in next_d:
                next_d.pop(n-1)

            b = boredom(next_d, memo) + n
            if b > max_points:
                max_points = b

        memo[str(d)] = max_points
        return max_points


if __name__ == '__main__':
    memo = {}
    print(boredom(c, memo))
    print(memo)