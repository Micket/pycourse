import numpy as np


class OuterMatrix:
    def __init__(self, x, y):
        self.x = x.copy()
        self.y = y.copy()

    def __getitem__(self, pos):
        row, col = pos
        if type(row) == slice and type(col) == slice:
            return OuterMatrix(self.x[row], self.y[col])
        else:
            return self.x[row] * self.y[col]

    def __mul__(self, value):
        if type(value) in [float, int]:
            return OuterMatrix(value*self.x, self.y)
        elif type(value) == np.ndarray:
            if len(value.shape) > 1:
                raise Exception("Can only multiply by 1D NumPy arrays")
            return np.dot(self.y, value) * self.x
        else:
            raise TypeError("Can only multiply by scalar or 1D NumPy arrays")

    def __imul__(self, value: float):
        if type(value) not in [float, int]:
            raise TypeError("Can only multiply by scalars")
        self.x *= value
        return self

    def norm(self):
        return np.linalg.norm(self.x) * np.linalg.norm(self.y)

    def transpose(self):
        return OuterMatrix(self.y, self.x)

    def toarray(self):
        return np.outer(self.x, self.y)


# Test
a = np.array([9., 1., 2., 3., 4., 5., 6.])
b = np.array([2., 1., 4., 3., 6., 5., 7.])
c = np.array([1., 2., 1., 7., 8., 2., 4.])

m = OuterMatrix(a, b)

print("Expanded:\n{}".format(m.toarray()))
m_sub = m[1:3, 2:5]  # This should also be a OuterMatrix.
print("Slicing (expanded):\n{}".format(m_sub.toarray()))
print("Slicing:", m[1:3, 5])  # slice + int -> ndarray
print("Slicing:", m[3, 2:5])  # int + slice -> ndarray
print("Item:", m[2, 4])  # int + int -> float
print("Norm:", m.norm())
m *= 2.0
print("Norm after scaling:", m.norm())
print("Multiplication with array:", m * c)
m_sub_t = m_sub.transpose()
print("Transpose (expanded):\n{}".format(m_sub_t.toarray()))
# Exceptions
#print(m * c.tolist())
#print(m * np.stack((c ,c)))
