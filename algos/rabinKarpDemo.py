target = "abb"
source = "ccabbabbcd"

PRIME = 319
BASE = 128


def hash_gen(target):
    h = 0
    for ch in target:
        # print(ch)
        h = (h * BASE + ord(ch)) % PRIME
    return h


target_hash = hash_gen(target)
# number of iterations len(source)-len(target)


# this value
RM = pow(BASE, len(target) - 1, PRIME)

# compute initial hash
h = 0
gen1 = iter(source)
gen2 = iter(source)
for i in range(len(target)):
    next(gen2)

for i in range(len(target)):
    h = (h * BASE + ord(source[i])) % PRIME

# compare initial hash with target hash
if h == target_hash:
    print(0)

j = -1
for i in range(len(source) - len(target)):
    # remove the first character and append a new character at the end
    h = ((h - ord(next(gen1)) * RM) * BASE + ord(next(gen2))) % PRIME
    if h == target_hash:
        j = i + 1
        break

print(j)
# print(h)
# sliding
# pow(R,2,PRIME) should only be computed once
