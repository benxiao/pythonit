import sympy


KEY = 0
VALUE = 1
SPECIAL_PRIMES = [
    19,
    43,
    67,
    131,
    263,
    523,
    1031,
    2063,
    4099,
    8219,
    16411,
    32771,
    65539,
    131111,
    262147,
    524347,
    1048583,
    2097211,
    4194319,
    8388619,
    16777259,
    33554467,
    67108879,
    134217779,
    268435459,
    536870923,
    1073741827,
    2147483659,
    4294967311,
    8589934627,
    17179869263,
    34359738451
]

__author__ = 'Ran Xiao'


class HashTableQP:

    THRESHOLD = 0.5
    # implement delete function

    OCCUPIED = 'O'

    def __init__(self, **kwargs):
        """
        :param kwargs:
        """
        # if the sz is set, the table will not resize
        sz = kwargs.get('sz')
        if sz:
            while sz % 4 != 3 or not sympy.isprime(sz):
                sz += 1
            HashTableQP.THRESHOLD = 1.1
            SPECIAL_PRIMES[0] = sz
        self._szi = 0
        self._array = [None] * SPECIAL_PRIMES[self._szi]
        self._used = 0
        self._a = kwargs.get('a') or 32771
        self._b = kwargs.get('b') or 27183
        # tracking collisions
        self._nc = 0

    def is_full(self):
        return self._used == SPECIAL_PRIMES[self._szi]

    def __len__(self):
        return self._used

    @property
    def n_collision(self):
        return self._nc

    def __getitem__(self, key):
        idx = self._find_pos_with(key)
        return self._array[idx][VALUE]

    def _setitem(self, key, value):
        sz = SPECIAL_PRIMES[self._szi]
        original_pos = self._hash(key)
        pos = original_pos
        for i in range(1, sz+1):
            if (self._array[pos] is None) or (self._array[pos] is HashTableQP.OCCUPIED):
                self._array[pos] = (key, value)
                return True
            else:
                k, _ = self._array[pos]
                if k == key:
                    self._array[pos] = (key, value)
                    return False
                else:
                    # alternate sign
                    if i % 2 == 0:
                        pos = (original_pos - i**2) % sz
                    else:
                        pos = (original_pos + i**2) % sz
                    self._nc += 1
        if self.is_full():
            raise ValueError('table is full')
        raise ValueError('key %s not inserted' % key, 'sz:', sz, 'used:', self._used)

    def __setitem__(self, key, value):
        if self._used / SPECIAL_PRIMES[self._szi] > HashTableQP.THRESHOLD:
            self._double_table()
        if self._setitem(key, value):
            self._used += 1

    def remove(self, key):
        idx = self._find_pos_with(key)
        self._array[idx] = HashTableQP.OCCUPIED
        self._used -= 1

    def _find_pos_with(self, key):
        sz = SPECIAL_PRIMES[self._szi]
        original_pos = self._hash(key)
        pos = original_pos
        for i in range(1, sz+1):
            if self._array[pos] is not None:
                if (self._array[pos] is HashTableQP.OCCUPIED) or (self._array[pos][KEY] != key):
                    if i % 2 == 0:
                        pos = (original_pos - i**2) % sz
                    else:
                        pos = (original_pos + i**2) % sz
                else:
                    return pos
            else:
                break
        raise KeyError('key %s not found' % key)

    def __contains__(self, key):
        try:
            self._find_pos_with(key)
            return True
        except KeyError:
            return False

    def _double_table(self):
        self._szi += 1
        old_array = self._array
        self._array = [None] * SPECIAL_PRIMES[self._szi]
        self._nc = 0
        for item in old_array:
            if item and (item is not HashTableQP.OCCUPIED):
                k, v = item
                self._setitem(k, v)

    def _hash(self, key):
        sz = SPECIAL_PRIMES[self._szi]
        value = 0
        a = self._a
        b = self._b
        for ch in key:
            value = (a * value + ord(ch)) % sz
            a = a * b % (sz-1)
        return value

    def __iter__(self):
        for node in self._array:
            if node is not None and node is not HashTableQP.OCCUPIED:
                k, _ = node
                yield k

    def __str__(self):
        return '{'+", ".join(x+': '+str(self[x]) for x in self)+'}'


if __name__ == '__main__':
    ht = HashTableQP()
    name_list = []
    for name in open('english_large.txt'):
        ht[name.rstrip()] = 1

    for name in open('english_large.txt'):
        ht.remove(name.rstrip())
    print(ht._nc)
    print(set(ht._array))
    print(ht._used)
