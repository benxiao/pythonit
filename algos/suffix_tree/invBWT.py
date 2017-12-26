from csort import kic_sort
import time

start = time.time()
text = "hd-$-__dnnhtoeesmsdn______uellbbvbhbiltcettlvhraeaeh_iAoKtDgoEiau_su_i_smner"
l = list(text)
length = len(l)
f = kic_sort(l)
rank = {}
for i, c in enumerate(f):
    if c not in rank:
        rank[c] = i

print(rank)
occurrences = [0] * length
temp = {}
for i, c in enumerate(l):
    if c in temp:
        occurrences[i] = temp[c]
        temp[c] += 1
    else:
        temp[c] = 1

print("occurrences ", occurrences)
print("rank ", rank)

pos = 0
i = 0
temp = []
while pos < length:
    ch = f[i]
    temp.append(ch)
    i = occurrences[i] + rank[l[i]]
    pos += 1
print("".join(reversed(temp)))

print(time.time() - start)



