# one dimension


a = [3, 0, 1, 7, 10, 2, 11]
a.sort()
closest = None
dist = float("inf")
for i in range(len(a)-1):
    if a[i+1] - a[i] < dist:
        dist = a[i+1] - a[i]
        closet = (a[i+1], a[i])

print(closet)


# divide and conquer
def close_pair_1d(a, lo, hi):
    if hi > lo + 4:
        mi = (hi+lo) // 2
        l_dist = close_pair_1d(a, lo, mi)
        r_dist = close_pair_1d(a, mi, hi)
        cross_dist = a[mi] - a[mi-1]
        return min(l_dist, r_dist, cross_dist)
    else:
        m_dist = float("inf")
        print(lo, hi-1)
        for i in range(lo, hi-1):
            m_dist = min(m_dist, a[i+1]-a[i])
        return m_dist





if __name__ == '__main__':
    a = [0,3,40,8,10,17,40,41,50,90]
    print(close_pair_1d(a, 0, len(a)))








