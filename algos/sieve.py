import math


def sieve(n):
    lst = list(range(2, n + 1))
    i = 0
    while i < len(lst):
        n = lst[i]
        lst = [x for x in lst if x % n != 0 or x == n]
        i += 1
    return lst


def sieve2(n):
    lst = list(range(2, n + 1))
    j = i = 0
    skip = 2
    it = 0
    while it < math.floor(math.sqrt(n)):
        while i + skip < len(lst):
            i += skip  # which is a prime
            lst[i] = None
        while not lst[j + 1]:
            j += 1
        skip = lst[j + 1]
        i = j + 1  # set start position for next iteration
        j += 1
        it = skip
    return lst


if __name__ == '__main__':
    import time

    start = time.time()
    lst2 = [x for x in sieve2(1000000) if x]
    print(lst2)
    print(time.time() - start)
