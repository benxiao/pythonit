class KeyAlreadyExists(Exception):
    """
    """
    pass


KEY = 0
PRIORITY = 1


class MyHeapDict:
    """
    """

    def __init__(self):
        """
        """
        self._heap = [(None, None)]
        self._dict = {}

    def __len__(self):
        """
        :return:
        """
        return len(self._heap) - 1

    @staticmethod
    def left(x):
        """
        :param x:
        :return:
        """
        return x << 1

    @staticmethod
    def right(x):
        """
        :param x:
        :return:
        """
        return (x << 1) + 1

    @staticmethod
    def parent(x):
        """
        :param x:
        :return:
        """
        return x >> 1

    def smaller_child(self, x):
        """
        :param x:
        :return:
        """
        # print(self.left(x), self.right(x), len(self))
        if self.left(x) == len(self) or self._heap[self.left(x)][PRIORITY] < self._heap[self.right(x)][PRIORITY]:
            return self.left(x)
        return self.right(x)

    def add(self, key, priority):
        """
        :param key:
        :param priority:
        :return:
        """
        if key in self._dict:
            raise KeyAlreadyExists()
        self._heap.append((key, priority))
        self._dict[key] = len(self)
        self.rise(len(self))

    def change_priority(self, key, priority):
        """
        :param key:
        :param priority:
        :return:
        """
        if not key in self._dict:
            raise KeyError()
        _, old = self._heap[self._dict[key]]
        self._heap[self._dict[key]] = (key, priority)
        if priority > old:
            self.sink(self._dict[key])
        else:
            self.rise(self._dict[key])

    def pop(self):
        """
        :return:
        """
        if len(self) == 0:
            raise ValueError()
        top = self._heap[1]
        self._dict.pop(top[KEY])
        last = self._heap.pop()
        self._heap[1] = last
        self._dict[last[KEY]] = 1
        self.sink(1)
        return top

    def peek(self):
        """
        :return:
        """
        if len(self) == 0:
            raise ValueError()
        return self._heap[1]

    def delete(self, key):
        """
        :param key:
        :return:
        """
        minimum = self._heap[1][PRIORITY]
        self.change_priority(key, minimum - 1)
        self.pop()

    def check_invariant(self):
        """
        :return:
        """
        for k in self._dict:
            assert k == self._heap[self._dict[k]][KEY]
        assert self.is_min_heap()

    def is_min_heap(self):
        """
        :return:
        """
        k = 1
        while self.right(k) <= len(self):
            child = self.smaller_child(k)
            if self._heap[child][PRIORITY] < self._heap[k][PRIORITY]:
                return False
            k += 1
        if self.left(k) == len(self) and self._heap[self.left(k)][PRIORITY] < self._heap[k][PRIORITY]:
            return False
        return True

    def rise(self, x):
        """
        :param x:
        :return: None
        """
        while self.parent(x) > 0:
            parent = self.parent(x)
            if self._heap[x][PRIORITY] >= self._heap[parent][PRIORITY]:
                break
            self._heap[x], self._heap[parent] = self._heap[parent], self._heap[x]
            nx = self._heap[x][KEY]
            np = self._heap[parent][KEY]
            self._dict[nx], self._dict[np] = self._dict[np], self._dict[nx]
            x = parent

    def sink(self, x):
        """
        :param x:
        :return:
        """
        while self.left(x) <= len(self):
            child = self.smaller_child(x)
            if self._heap[child][PRIORITY] > self._heap[x][PRIORITY]:
                break
            self._heap[child], self._heap[x] = self._heap[x], self._heap[child]
            nx = self._heap[x][KEY]
            nc = self._heap[child][KEY]
            self._dict[nx], self._dict[nc] = self._dict[nc], self._dict[nx]
            x = child

    def clear(self):
        self._heap.clear()
        self._dict.clear()


if __name__ == '__main__':
    import random
    import heapdict
    import time

    random.seed(0)
    hd = MyHeapDict()
    hd2 = heapdict.heapdict()

    lst = list(range(1000000))
    start = time.time()
    random.shuffle(lst)
    # for e in lst:
    #     hd.add(e,e)

    for e in lst:
        hd2[e] = e

    print(time.time() - start)
