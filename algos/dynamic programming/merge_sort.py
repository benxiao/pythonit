import operator

def merge_sort(lst, key=None):
    if key is None: comparator = operator.lt
    else: comparator = lambda x, y: key(x) < key(y)

    l = len(lst)
    increment = 1
    while increment < l:
        for i in range(0,l,increment*2):
            if i+increment*2 < l:
                merge(lst, i, i+increment, i+increment*2, comparator)
            elif i+increment < l:
                merge(lst, i, i+increment, l, comparator)
        increment *= 2


def merge(lst, start, mid, end, comparator):
    tmp = [None] * (end-start)
    li = start
    le = mid
    ri = mid
    re = end
    ti = -1

    while li < le and ri < re:
        ti += 1
        if comparator(lst[li], lst[ri]):
            tmp[ti] = lst[li]
            li += 1
        else:
            tmp[ti] = lst[ri]
            ri += 1

    while li < le:
        ti += 1
        tmp[ti] = lst[li]
        li += 1

    while ri < re:
        ti += 1
        tmp[ti] = lst[ri]
        ri += 1

    for i in range(len(tmp)):
        lst[start+i] = tmp[i]

if __name__ == '__main__':
    import random
    import operator
    n = 1000
    lst = list(range(n))
    lst1 = list(range(n))
    random.shuffle(lst)
    random.shuffle(lst1)
    lst2 = list(zip(lst, lst1))
    # print(lst2)
    merge_sort(lst2, key=operator.itemgetter(0))

    print(lst2)
    merge_sort(lst2, key=operator.itemgetter(1))
    print("\n" * 3)
    print(lst2)
    merge_sort(lst2, key=lambda x: x[0]+x[1])
    print("\n" * 3)
    print(lst2)
    merge_sort(lst2, key=lambda x: abs(x[0]-500))
    print("\n" * 3)
    print(lst2)
    merge_sort(lst2, key=lambda x: abs(x[0]-x[1]))
    print("\n"*3)
    print(lst2)