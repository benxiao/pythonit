from tree import Node
INT_MAX = 2 ** 32

def opt_cost(freq, i, j):
    if j < i:
        return 0
    if j == i:
        return freq[i]
    # print(i,j+1)aaa
    fsum = sum(freq[i:j+1])
    # print(freq[i:j+1])
    # print(sum(freq[i:j+1]))

    min_cost = 2 ** 32
    for k in range(i, j+1):
        cost_left = opt_cost(freq, i, k-1)
        # print("cost_left", cost_left)
        cost_right = opt_cost(freq, k+1, j)
        # print("cost_right", cost_right)
        cost = cost_left + cost_right

        print("cost", i, j, cost)
        if min_cost > cost:
            min_cost = cost
    print("min_cost", min_cost)
    return min_cost + fsum


if __name__ == '__main__':
    print(opt_cost([34,8,50], 0, 2))
