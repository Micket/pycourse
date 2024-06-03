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