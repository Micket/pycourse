import numpy as np


# Tests for your code
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
