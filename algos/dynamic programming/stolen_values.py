values = [60, 100, 120]
wt = [10, 20, 30]
l = len(values)
cache_values = [0] * l
cache_weight =[0] * l
limit = 50


def napsack(values, wt, i, capacity):
    if i == 0:
        if capacity >= wt[0]:
            return values[0]
        else:
            return 0

    leave = napsack(values, wt, i-1, capacity)
    if capacity < wt[i]:
        return leave
    take = napsack(values, wt, i-1, capacity-wt[i]) + values[i]
    return max(leave, take)








if __name__ == '__main__':
    print(napsack(values, wt, 2, 50))





