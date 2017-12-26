def itemgetter(i):
    def func(arr):
        return arr[i]
    return func


if __name__ == '__main__':
    f = itemgetter(0)
    lst = [312, 123, 278]
    print(f(lst))