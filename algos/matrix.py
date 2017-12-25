class Matrix:
    def __init__(self, data):
        self._data = data
        r = len(self._data)
        c = len(self._data[0])
        self._shape = (r, c)

    def set_val(self, i, j, val):
        self._data[i][j] = val

    def get_val(self, i, j):
        return self._data[i][j]

    def __str__(self):
        return "[" + ",\n".join(str(row) for row in self._data) + "]"

    @staticmethod
    def ones(r, c):
        return Matrix([[1] * c for _ in range(r)])

    @staticmethod
    def zeroes(r, c):
        return Matrix([[0] * c for _ in range(r)])

    def get_row(self, i):
        return self._data[i][:]

    def get_col(self, i):
        return [x[i] for x in self._data]

    def shape(self):
        return self._shape

    @staticmethod
    def dot(x0, x1):
        return sum([x * y for x, y in zip(x0, x1)])

    def copy(self):
        r, c = self.shape()
        m = Matrix.zeroes(r, c)
        for i in range(r):
            for j in range(c):
                m.set_val(i, j, self.get_val(i, j))
        return m

    def __add__(self, other):
        if isinstance(other, Matrix):
            r0, c0 = self.shape()
            r1, c1 = other.shape()
            assert r0 == r1 and c0 == c1
            m = Matrix.zeroes(r0, c0)
            for i in range(r0):
                for j in range(c0):
                    val = self.get_val(i, j) + other.get_val(i, j)
                    m.set_val(i, j, val)
            return m

        elif isinstance(other, (float, int)):
            r, c = self.shape()
            m = Matrix.zeroes(r, c)
            for i in range(r):
                for j in range(c):
                    m.set_val(i, j, self.get_val(i, j) + other)
            return m

    def __sub__(self, other):
        if isinstance(other, Matrix):
            r0, c0 = self.shape()
            r1, c1 = other.shape()
            assert r0 == r1 and c0 == c1
            m = Matrix.zeroes(r0, c0)
            for i in range(r0):
                for j in range(c0):
                    val = self.get_val(i, j) - other.get_val(i, j)
                    m.set_val(i, j, val)
            return m
        elif isinstance(other, (float, int)):
            r, c = self.shape()
            m = Matrix.zeroes(r, c)
            for i in range(r):
                for j in range(c):
                    m.set_val(i, j, self.get_val(i, j) - other)
            return m

    def __mul__(self, other):
        if isinstance(other, Matrix):
            r0, c0 = self.shape()
            r1, c1 = other.shape()
            assert c0 == r1
            m = Matrix.zeroes(r0, c1)
            for i in range(r0):
                for j in range(c1):
                    row = self.get_row(i)
                    col = other.get_col(j)
                    val = self.dot(row, col)
                    m.set_val(i, j, val)
            return m
        elif isinstance(other, (float, int)):
            r, c = self.shape()
            m = self.copy()
            for i in range(r):
                for j in range(c):
                    m.set_val(i, j, m.get_val(i, j) * other)
            return m
        else:
            raise TypeError("other is of {}".format(str(type(other))))


if __name__ == '__main__':
    m1 = Matrix([[9], [8], [7]])
    m2 = Matrix([[1, 2, 3], [4, 5, 6]])
    print(m2 * m1)
    m1 = Matrix([[1, 3, 5, 7], [2, 4, 6, 8]])
    m2 = Matrix([[1, 8, 9], [2, 7, 10], [3, 6, 11], [4, 5, 12]])
    print(m1 * m2)

    m3 = Matrix.ones(2, 2)
    m4 = Matrix.ones(2, 2)
    print(m3 + 4)
    print(m3 - 4)
