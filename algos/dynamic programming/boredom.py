a = [1, 2, 1, 3, 2, 2, 2, 2, 3]
b  = [2, 2, 2, 2]
def boredom(a):
    if not a:
         return 0
    max_points = 0
    for i, n in enumerate(a):
        next_lst = a[:]
        next_lst.pop(i)
        next_lst = list(filter(lambda x: x != n+1 and x != n-1, next_lst))
        b = boredom(next_lst) + n
        if b > max_points:
            max_points = b
    return max_points

if __name__ == '__main__':
    print(boredom(a))