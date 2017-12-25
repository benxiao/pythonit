"""
find the square root of integer using newton's method

"""
import math
import random
import time
from collections import Counter


def newton_sqrt(x, tolerance=None):
    # initial guess
    x0 = x
    if not tolerance:
        tolerance = 1.0 / 1000000
    update = lambda n: n - 0.5 * n + x / (2 * n)
    x1 = update(x0)
    # check convergence
    while abs(x0 - x1) > tolerance:
        x0 = x1
        x1 = update(x0)
    return x1


def newton_sqrtt(x, tolerance=None):
    x0 = x
    if not tolerance:
        tolerance = 1.0 / 1000000
    update = lambda n: n - n / 3 + x / (3 * n * n)
    x1 = update(x0)
    # check convergence
    while abs(x0 - x1) > tolerance:
        x0 = x1
        x1 = update(x0)
    return x1


def weighted_choice(multinomial_dist):
    assert isinstance(multinomial_dist, dict)
    assert all(isinstance(v, int) for _, v in multinomial_dist.items())
    assert all(v >= 0 for _, v in multinomial_dist.items())
    labels = list(multinomial_dist.keys())
    cumsum = [0]
    for l in labels:
        cumsum.append(cumsum[-1] + multinomial_dist[l])
    index = random.randint(1, cumsum[-1])
    chosen = None
    for i in range(len(cumsum) - 1):
        if cumsum[i] < index <= cumsum[i + 1]:
            chosen = i
            break
    return labels[chosen]


class WeightedChoice:
    def __init__(self, multinomial_dist):
        assert isinstance(multinomial_dist, dict)
        assert all(isinstance(v, int) for _, v in multinomial_dist.items())
        assert all(v >= 0 for _, v in multinomial_dist.items())
        self._labels = list(multinomial_dist.keys())
        self._cumsum = [0]
        for l in self._labels:
            self._cumsum.append(self._cumsum[-1] + multinomial_dist[l])

    def get(self):
        cumsum = self._cumsum
        index = random.randint(1, cumsum[-1])
        chosen = None
        for i in range(len(cumsum) - 1):
            if cumsum[i] < index <= cumsum[i + 1]:
                chosen = i
                break
        return self._labels[chosen]


def longest_common_subsequence(s0, i0, s1, i1):
    if i0 == len(s0) or i1 == len(s1):
        return 0
    else:
        if s0[i0] == s1[i1]:
            return 1 + longest_common_subsequence(s0, i0 + 1, s1, i1 + 1)
        else:
            return max(longest_common_subsequence(s0, i0 + 1, s1, i1),
                       longest_common_subsequence(s0, i0, s1, i1 + 1))


if __name__ == '__main__':
    print(newton_sqrtt(1000))
    wc = WeightedChoice({'a': 5, 'b': 1, 'c': 5})
    start = time.time()
    print(Counter([wc.get() for _ in range(10000)]))
    # print(Counter([weighted_choice({'a':5, 'b':1, 'c':5}) for _ in range(10000)]))
    print(time.time() - start)

    print(longest_common_subsequence('abc', 0, 'acd', 0))
