class OneHotVector:
    def __init__(self, length, index):
        if index >= length:
            raise IndexError("index can not exceed length")
        self.length = length
        self.index = index

    def __len__(self):
        return self.length

    def __getitem__(self, item):
        if item < 0:
            item += len(self)
        if item < 0 or item >= self.length:
            raise IndexError("out of bounds")
        return 1 if item == self.index else 0

    def dot(self, matrix):
        if matrix.shape[0] != self.length:
            raise IndexError("incompatible matrix size")

        return matrix[self.index, :]

    def toarray(self, dtype=int):
        x = np.zeros(self.length, dtype=dtype)
        x[self.index] = 1
        return x

    def __repr__(self):
        return f'OneHotVector(length={self.length}, index={self.index})'


# Test code
import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])

v = OneHotVector(length=3, index=2)
w = OneHotVector(length=4, index=1)
u = OneHotVector(length=1000000000000, index=0)

print(u)

assert len(v) == 3

assert w[0] == 0
assert w[1] == 1
assert w[2] == 0

assert w[-3] == 1
assert w[-2] == 0

print(f'v as np.array: {v.toarray()}')
print(f'w as float np.array: {w.toarray(dtype=float)}')

print('v . a =', v.dot(a))
print('w . b =', w.dot(b))
