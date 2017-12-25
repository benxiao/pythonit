def quick_select(lst, s, e, nth):
    assert s <= nth < e
    p = partition(lst, s, e)
    print(p)
    if p == nth:
        return p
    if p < nth:
        return quick_select(lst, p + 1, e, nth)
    else:
        return quick_select(lst, s, p, nth)


def partition(lst, s, e):
    # pick first element as the pivot
    i, p = s, s
    pivot_v = lst[s]
    while i < e - 1:
        i += 1
        if lst[i] < pivot_v:
            p += 1
            lst[i], lst[p] = lst[p], lst[i]
    lst[p], lst[s] = lst[s], lst[p]
    return p


def isort(lst, s, e):
    i = s + 1
    while i < e:
        j = i
        temp = lst[j]

        while j > 0 and lst[j-1] > temp:
            lst[j] = lst[j - 1]
            j -= 1

        lst[j] = temp
        i += 1


def mm_quick_select(lst, s, e, nth):
    pass


if __name__ == '__main__':
    lst = [6, 1, 2, 3, 8, 10, 12, 10]
    print(isort(lst, 0, len(lst)))
    print(lst)
