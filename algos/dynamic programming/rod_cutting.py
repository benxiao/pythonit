n = 4
length = [1, 2, 3, 4]
price = [1, 5, 8, 9]
l = len(length)

def max_return(n):
    if n == 0:
        return 0

    potentials = []
    for i in range(l):
        if n >= length[i]:
            potentials.append(max_return(n-length[i])+price[i])
    return max(potentials)

print(max_return(4))