import matplotlib.pyplot as plt
import random
import math
from operator import itemgetter

# random.seed(0)


def generate_points(n):
    lst = []
    for i in range(n):
        lst.append((random.random(), random.random()))
    return lst


lst = generate_points(20)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter([x[0] for x in lst], [x[1] for x in lst])


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1-x2)**2 +(y1-y2)**2)


def find_bounds(lst, mid, margin):
    median, _ = lst[mid]
    low_limit, high_limit = max(0,median-margin), median+margin
    #print(low_limit, high_limit)
    low = mid
    #print(margin)
    while low > 0 and lst[low][0] > low_limit:
        low -= 1
    high = mid
    while high < len(lst) and lst[high][0] < high_limit :
        high += 1
    return low, high


# points are already sorted
def closestpair(points, start, end):
    if end-start < 20:
        return naive_closest_pair(points, start, end)

    mid = (start+end) // 2
    d1 = closestpair(points, start, mid)
    d2 = closestpair(points, mid, end)
    d = min(d1, d2)
    #print('margin:', d)
    low, high = find_bounds(lst, mid, d)
    #print(low, high)
    for i in range(low, high):
        j = 1
        while j < 8 and i+j < len(points):
            d = min(dist(points[i], points[i+j]), d)
            j += 1
    return d


def naive_closest_pair(lst, start, end):
    if end - start <= 2:# guarantee to have at least two points
        return float('inf')
    mininum = dist(lst[start], lst[start+1])
    for i in range(start, end):
        for j in range(i+1, end):
            current = dist(lst[i], lst[j])
            if current < mininum:
                mininum = current
    return mininum



if __name__ == '__main__':
    lst = generate_points(2000)
    lst.sort(key=itemgetter(0))
    # print(lst)

    print(closestpair(lst, 0, len(lst)))
    print(naive_closest_pair(lst, 0, len(lst)))





