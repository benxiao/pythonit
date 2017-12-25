KEY = 0
VALUE = 1
__author__ = 'Ran Xiao'


class HashTableLP:
    DEFAULT_SIZE = 8
    THRESHOLD = .5
    # implement delete function

    OCCUPIED = 'O'

    def __init__(self, **kwargs):
        """
        :param kwargs:
        """
        self._sz = kwargs.get('sz') or HashTableLP.DEFAULT_SIZE
        self._array = [None] * self._sz
        self._used = 0
        self._a = kwargs.get('a') or 32771
        self._b = kwargs.get('b') or 27183
        self._pi = kwargs.get('pi') or 1  # probing interval
        self._nc = 0

    def is_full(self):
        return self._used == self._sz

    def __len__(self):
        return self._used

    @property
    def n_collision(self):
        return self._nc

    def __getitem__(self, key):
        idx = self._find_pos_with(key)
        return self._array[idx][VALUE]

    def _setitem(self, key, value):
        pos = self._hash(key)
        for _ in range(self._sz):
            if (self._array[pos] is None) or (self._array[pos] is HashTableLP.OCCUPIED):
                self._array[pos] = (key, value)
                return True
            else:
                k, _ = self._array[pos]
                if k == key:
                    self._array[pos] = (key, value)
                    return False
                else:
                    pos = (pos + self._pi) % self._sz
                    self._nc += 1
        raise ValueError('key %s not inserted')

    def __setitem__(self, key, value):
        if self._used / self._sz >= HashTableLP.THRESHOLD:
            self._double_table()
        if self._setitem(key, value):
            self._used += 1

    def remove(self, key):
        idx = self._find_pos_with(key)
        self._array[idx] = HashTableLP.OCCUPIED
        self._used -= 1

    def _find_pos_with(self, key):
        pos = self._hash(key)
        for _ in range(self._sz):
            if self._array[pos] is not None:
                if (self._array[pos] is HashTableLP.OCCUPIED) or (self._array[pos][KEY] != key):
                    pos = (pos + self._pi) % self._sz
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
        self._sz *= 2
        old_array = self._array
        self._array = [None] * self._sz
        self._nc = 0
        for item in old_array:
            if item and (item is not HashTableLP.OCCUPIED):
                k, v = item
                self._setitem(k, v)

    def _hash(self, key):
        value = 0
        a = self._a
        b = self._b
        for ch in key:
            value = (a * value + ord(ch)) % self._sz
            a = a * b % (self._sz-1)
        return value

    def __iter__(self):
        for node in self._array:
            if node is not None and node is not HashTableLP.OCCUPIED:
                k, _ = node
                yield k

    def __str__(self):
        return '{'+", ".join(x+': '+str(self[x]) for x in self)+'}'


if __name__ == '__main__':
    ht = HashTableLP()
    name_list = ['obama','trump','clinton','romney', 'micelle','hilary']
    for name in name_list:
        ht[name.rstrip()] = 1

    print(ht)

    ht = HashTableLP()
    # name_list = []
    # for name in open('english_large.txt'):
    #     ht[name.rstrip()] = 1
    #
    # for name in open('english_large.txt'):
    #     ht.remove(name.rstrip())
    #
    # print(ht._nc)


