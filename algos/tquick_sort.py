constant = 20


def t_partition(arr, lo, hi):
    l = lo
    h = hi - 1
    pivot_value = arr[lo]
    mid = lo
    while h > mid:
        if arr[mid] < pivot_value:
            arr[l], arr[mid] = arr[mid], arr[l]
            l += 1
            mid += 1

        elif arr[mid] == pivot_value:
            mid += 1

        else:
            arr[mid], arr[h] = arr[h], arr[mid]
            h -= 1

    return (l, mid)


def quick_sort_aux(arr, lo, hi):
    if hi > lo + constant:
        l, m = t_partition(arr, lo, hi)
        quick_sort_aux(arr, lo, l)
        quick_sort_aux(arr, m, hi)


def quick_sort(arr):
    quick_sort_aux(arr, 0, len(arr))
    insort(arr)

def insort(array):
    l = len(array)
    for i in range(1, l):
        v = array[i]
        j = i
        while j > 0 and array[j - 1] > v:
            array[j] = array[j - 1]
            j -= 1
        array[j] = v


def dutch_flag(arr):
    lo = 0
    mid = 0
    end = len(arr) - 1

    while end > mid:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1

        elif arr[mid] == 2:
            arr[mid], arr[end] = arr[end], arr[mid]
            end -= 1
    print(arr)
    return lo, mid

if __name__ == '__main__':
    import random
    import time
    for i in range(5, 35):
        samples = []
        constant = i
        for _ in range(10):
            start = time.time()
            lst = [random.randint(0, 1000) for _ in range(500000)]
            random.shuffle(lst)
            quick_sort(lst)
            samples.append(time.time() - start)

        print(i, sum(samples) / len(samples))