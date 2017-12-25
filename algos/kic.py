import random
random.seed(0)

"""
* * * key index counting * * *
"""

N = 20
RANGE = 256
array_integer = [random.randint(0, 20) for _ in range(N)]
result = [None] * N
freq = [0] * (RANGE+1)  # one above the necessary
l = len(array_integer)
aux = [None] * l

for ch in array_integer:
    freq[ch+1] += 1

for i in range(1, len(freq)):
    freq[i] += freq[i-1]

for ch in array_integer:
    aux[freq[ch]] = ch
    freq[ch] += 1

array_integer, aux = aux, array_integer
print(array_integer)
