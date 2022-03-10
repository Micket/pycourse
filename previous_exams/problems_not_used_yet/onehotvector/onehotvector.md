# Question 3: OneHotVector (6p)
In some applications there is a need for a special vector where only a single element is set to 1, the rest being zero.
The is typically called a `OneHotVector`.

## Task A (1p)

Create the class `OneHotVector` that takes a length and an index of the nonzero element.

## Task B (0.5p)
Add a nice looking `repr` implementation.

## Task C (0.5p)
Implement support for `len(x)` on your `OneHotVector`.

## Task D (1p)
Implement support for scalar indexing (just getting the items, not assignment)
Also add support so that negative indexes work (starting from the end).

## Task E (1p)

Add the method `toarray` which returns the a numpy array version of this vector.
Have it take an optional argument of what datatype to use in the numpy array, with a default value of `np.int`

## Task F (1.5p)

TODO: decide
Implement support for a dot product between the vector and a matrix (numpy array) by adding a `dot` method that computes $v \cdot M$ for a vector $v$ and matrix $M$.
Since where is just 1 nonzero value, this simply means extracting the corresponding row which can be done very efficiently.

PROBLEMATIC due to single-dispatch mechanism:
Implement support for "left" and "right multiplikation with a matrix (numpy array).
Since where is just 1 nonzero value, this simply means extracting one column or row respectively.

## Task G 1p

Add bounds checking to task A, B, C and D and raise an `IndexError` with appropriate messages when indices or dimensions don't match.

**Example**
```python
import numpy as np

a = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
b = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

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

print(f'v as np.array: {w.toarray()}')
print(f'w as float np.array: {w.toarray(dtype=float)}')

print('v . a =', v.dot(a))
print('w . b =', w.dot(b))
```

**Output**
```text
OneHotVector(length=1000000000000, index=0)
v as np.array: [0 1 0 0]
w as float np.array: [0. 1. 0. 0.]
v . a = [7 8 9]
w . b = [5 6 7 8]
```
