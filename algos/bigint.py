import random

convert = lambda arr: int(''.join(str(x) for x in arr), base=2)


class BigInt(list):
    def __init__(self, iterable):
        super(BigInt, self).__init__(iterable)
        assert all(x in (0, 1) for x in self)

    def __str__(self):
        return str(convert(self))

    __repr__ = __str__


def add(x, y):
    if len(x) < len(y):
        x, y = y, x
    r = []
    carrying_bit = 0
    diff = len(x) - len(y)
    for i in reversed(range(len(y))):
        v = x[i + diff] + y[i] + carrying_bit
        carrying_bit = v >> 1
        r.append(v % 2)
    for i in reversed(range(diff)):
        v = x[i] + carrying_bit
        carrying_bit = v >> 1
        r.append(v % 2)
    if carrying_bit == 1:
        r.append(1)
    return BigInt(reversed(r))


def mul(x, y):
    if isZero(x) or isZero(y):
        return BigInt([0])
    if isOne(y):
        return BigInt(x)
    v = mul(x, half(y))
    if isOdd(y):
        return add(add(v, v), x)
    else:
        return add(v, v)


def isOdd(x):
    return x[-1] == 1


def half(x):
    x = x[:]
    if len(x) > 1:
        x.pop()
    else:
        x.pop()
        x.append(0)
    return x


def isZero(x):
    return len(x) == 1 and x[0] == 0


def isOne(x):
    return len(x) == 1 and x[0] == 1


if __name__ == '__main__':
    x = BigInt([random.randint(0, 1) for i in range(200)])
    y = BigInt([random.randint(0, 1) for i in range(200)])
    print(x, y)
    print(mul(x, y))
    assert convert(x) * convert(y) == convert(mul(x, y))
