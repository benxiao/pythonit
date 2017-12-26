def count_inversions(lst):
    lst_copy = list(lst)
    temp = [None] * len(lst_copy)
    return count_inversions_aux(lst_copy, 0, len(lst_copy), temp)


def count_inversions_aux(lst, start, end, temp):
    if end-start < 2:
        return 0
    mid = (start+end)//2
    left = count_inversions_aux(lst, start, mid, temp)
    right = count_inversions_aux(lst, mid, end, temp)
    cross = count_cross_inversions(lst, start, mid, end, temp)
    return left+right+cross


def count_cross_inversions(lst, start, mid, end, temp):
    inversions = 0
    li, ri = start, mid
    ti = start

    while (li < mid) and (ri < end):
        if lst[li] < lst[ri]:
            temp[ti] = lst[li]
            li += 1
            ti += 1

        else:
            temp[ti] = lst[ri]
            ri += 1
            ti += 1
            inversions += (mid-li)

    while (li < mid):
        temp[ti] = lst[li]
        li += 1
        ti += 1

    while (ri < end):
        temp[ti] = lst[ri]
        ri += 1
        ti += 1
        inversions += (mid-li)

    for i in range(start, end):
        lst[i] = temp[i]

    return inversions


if __name__ == '__main__':
    for i in range(1,20):
        lst = list(range(i, 0, -1))
        print(count_inversions(lst))