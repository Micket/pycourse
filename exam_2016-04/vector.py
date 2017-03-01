from math import sqrt


class BaseVector:
    def norm(self):
        raise NotImplementedError("Norm functionality missing")

    def slice(self, start, end):
        raise NotImplementedError("Slicing functionality missing")


class ZeroVector(BaseVector):
    def __init__(self, size):
        self.size = size

    def __len__(self):
        return self.size

    def __getitem__(self, item):
        if item < 0 or item > self.size:
            raise IndexError("Index {} outside range for size {}".format(item, len(self)))
        return 0.

    def norm(self):
        return 0.

    def slice(self, start, end):
        return ZeroVector(end - start)


class Vector(BaseVector):
    def __init__(self, values):
        self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        return self.values[item]

    def norm(self):
        x = 0.
        for v in self.values:
            x += v*v
        return sqrt(x)

    def slice(self, start, end):
        # Optional:
        if start > len(self) or end > len(self):
            raise IndexError("Slice index {},{} outside range".format(start, end) )
        return VectorSlice(self, start, end)


class VectorSlice(BaseVector):
    def __init__(self, vector, start, end):
        self.values = vector
        self.start = start
        self.end = end

    def __len__(self):
        return self.end - self.start

    def __getitem__(self, item):
        if item < 0 or item > len(self):
            raise IndexError("Index {} outside range for size {}".format(item, len(self)))
        return self.vector[self.start + item]

    def norm(self):
        x = 0.
        for i in range(self.start, self.end):
            x += self.vector[i] ** 2
        return sqrt(x)

    def slice(self, start, end):
        # Optional:
        if start > len(self) or end > len(self):
            raise IndexError("Slice index {},{} outside range".format(start, end) )
        return VectorSlice(self.vector, self.start + start, self.start + end)