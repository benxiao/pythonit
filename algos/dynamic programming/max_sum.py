# Maximum sum of all sub-arrays
# always

lst = [0, 10, 3, -4, 1, 0, 2]
lst2 = [0, 1, -2, 3, 10, -4, 7, 2, -5]
cumsum = lst[:]
l = len(lst)
for i in range(1, l):
    cumsum[i] += cumsum[i-1]
print(cumsum)

max_val = 0
for i in range(l):
    for j in range(i+1, l):
        val = cumsum[j] - cumsum[i]
        if val > max_val:
            max_val = val
print(max_val)







