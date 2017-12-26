class Grid:
    def __init__(self, r, c, default=None):
        self._default = default
        self._array = [self._default] * (r * c)
        self._r = r
        self._c = c

    def copy(self):
        copied = Grid(self._r, self._c)
        copied._array = self._array[:]
        return copied

    @property
    def shape(self):
        return self._r, self._c

    def __len__(self):
        return self._r * self._c

    def ascii_art(self, space=8):
        rows = []
        for i in range(self._r):
            rows.append(' '.join(str(item).center(space) for item in self._array[i*self._c:(i+1)*self._c]))
        return '\n'.join(rows) + '\n'

    def get(self, r, c):
        if not self.out_of_bounds(r, c):
            return self._array[r*self._c+c]
        return 0

    def set(self, new_val, r, c):
        self._validate_accessor(r, c)
        self._array[r*self._c+c] = new_val

    def set_row(self, new_val, r):
        self._validate_accessor(r, 0)
        for i in range(self._c):
            self.set(new_val, r, i)

    def set_col(self, new_val, c):
        self._validate_accessor(0, c)
        for i in range(self._r):
            self.set(new_val, i, c)

    def reset(self):
        for i in range(len(self)):
            self._array[i] = self._default

    def out_of_bounds(self, r, c):
        return (r < 0 or r >= self._r) or (c < 0 or c >= self._c)

    def _validate_accessor(self, r, c):
        if self.out_of_bounds(r, c):
            raise IndexError()

if __name__ == '__main__':
    grid = Grid(12, 12, 1)
    grid.set_row(2, 0)
    grid.set_col(2, 0)
    print(grid.ascii_art())
    r, c = grid.shape
    for k in range(1, r):
        i = -1
        for j in range(k, r):
            i += 1
            grid.set(0, i, j)
        print(grid.ascii_art())