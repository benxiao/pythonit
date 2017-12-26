def qsort(a, i, j):
    if j-i > 1:
        p = partition(a, i, j)
        qsort(a, p+1, j)
        qsort(a, i, p)


def partition(a, i, j):
    p = i
    f = i
    p_v = a[p]
    print(p_v)
    while f < j-1:
        f += 1
        if a[f] < p_v:
            p += 1
            a[f], a[p] = a[p], a[f]

    a[p], a[i] = a[i], a[p]
    return p


if __name__ == '__main__':
    lst = [3,1,2,6,7]

    print(partition(lst, 0 , 5))
    qsort(lst, 0, 5)
    print(lst)


