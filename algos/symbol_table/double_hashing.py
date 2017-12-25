import sympy
__author__ = 'Ran Xiao'

KEY = 0
VALUE = 1


PRIMES = [
    11,
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


class HashTableDH:
    THRESHOLD = 0.6
    # implement delete function

    OCCUPIED = 'O'

    def __init__(self, **kwargs):
        """
        :param kwargs:
        """
        sz = kwargs.get('sz')
        if sz:
            # find a prime close to that number
            while not sympy.isprime(sz):
                sz += 1
            # when the space is specified disable table doubling
            HashTableDH.THRESHOLD = 1.1
            PRIMES[0] = sz
        self._szi = 0
        self._array = [None] * PRIMES[self._szi]
        self._used = 0
        self._a = kwargs.get('a') or 53299
        self._b = kwargs.get('b') or 30417
        self._nc = 0

    def is_full(self):
        return self._used == len(self._array)

    def __len__(self):
        return self._used

    @property
    def n_collision(self):
        return self._nc

    def __getitem__(self, key):
        idx = self._find_pos_with(key)
        return self._array[idx][VALUE]

    def _setitem(self, key, value):
        pos = self._first_hash(key)
        step = self._second_hash(key)
        for _ in range(len(self._array)):
            if (self._array[pos] is None) or (self._array[pos] is HashTableDH.OCCUPIED):
                self._array[pos] = (key, value)
                return True
            else:
                k, _ = self._array[pos]
                if k == key:
                    self._array[pos] = (key, value)
                    return False
                else:
                    pos = (pos+step) % len(self._array)
                    self._nc += 1
        raise ValueError('key: ', key, pos, step, len(self._array))

    def __setitem__(self, key, value):
        if self._used / len(self._array) >= HashTableDH.THRESHOLD:
            self._double_table()

        if self._setitem(key, value):
            self._used += 1

    def remove(self, key):
        # allow find_pos_with to raise KeyError
        idx = self._find_pos_with(key)
        self._array[idx] = HashTableDH.OCCUPIED
        self._used -= 1

    def _find_pos_with(self, key):
        pos = self._first_hash(key)
        step = self._second_hash(key)
        for _ in range(len(self._array)):
            if self._array[pos] is not None:
                if (self._array[pos] is HashTableDH.OCCUPIED) or (self._array[pos][KEY] != key):
                    pos = (pos + step) % len(self._array)
                else: return pos
            else: break
        raise KeyError('key %s not found' % key)

    def __contains__(self, key):
        try:
            self._find_pos_with(key)
            return True
        except KeyError:
            return False

    def _double_table(self):
        print('doubled')
        print(self._used)
        self._szi += 1
        old_array = self._array
        self._array = [None] * PRIMES[self._szi]
        self._nc = 0
        for item in old_array:
            if item and (item is not HashTableDH.OCCUPIED):
                k, v = item
                self._setitem(k, v)
        print(self._used)

    def _first_hash(self, key):
        value = 0
        a = self._a
        b = self._b
        for ch in key:
            value = (a * value + ord(ch)) % len(self._array)
            a = a * b % len(self._array)
        return value

    def _second_hash(self, key):
        """
        second hash function
        cannot produce 0 as it will be used as the step, if the hash is 0, hash is changed to 1
        :param key:
        :return:
        """
        value = 0
        a = 59757
        b = 64587
        for ch in key:
            value = (a * value + ord(ch)) % len(self._array)
            a = a * b % len(self._array)
        return value or 6

    def __iter__(self):
        for node in self._array:
            if node is not None and node is not HashTableDH.OCCUPIED:
                k, _ = node
                yield k

    def __str__(self):
        return '{'+", ".join(x+': '+str(self[x]) for x in self)+'}'


if __name__ == '__main__':
    ht = HashTableDH()
    name_list = []
    s = 0
    for name in open('english_large.txt'):
        ht[name.rstrip()] = 1
        s += 1
    print(s)

    for name in open('english_large.txt'):
        ht.remove(name.rstrip())
    print(set(ht._array))
    print(ht._nc)