import numpy as np

class MatrixSizeMismatch(Exception):
    pass

class ConstrainedMatrix:
    def __init__(self, k, g):
        if k.shape[1] != g.shape[0] or k.shape[0] != g.shape[0]:
            raise MatrixSizeMismatch("Incompatible matrices: k = {}x{} but g has {} rows".format(*k.shape, g.shape[0]))

        self.k = k
        self.g = g

    def size(self):
        rows = k.shape[0] + g.shape[1]
        cols = k.shape[1] + g.shape[1]
        return (rows, cols)

    def dot_product(self, x):
        pos = k.shape[1]
        # It would be find to implement as a nested loop as well:
        v_k = np.dot(self.k, x[:pos]) + np.dot(self.g, x[pos:])
        v_g = np.dot(x[:pos], self.g)
        return np.concatenate((v_k, v_g))


# Small random test case:

k = np.array([[1,2,3],[4,5,6],[7,8,9]])
g = np.array([[1,0],[0,-1],[-1,1]])
x = np.array([1,0,2,3,0])

a = ConstrainedMatrix(k, g)
v = a.dot_product(x) 
print(v) # should be [10, 16, 22, -1, 2]

# This should raise an exception:
k2 = np.array([[1,2],[3,4],[5,6]])
try:
    b = ConstrainedMatrix(k2, g)
except MatrixSizeMismatch:
    print("doh")
    raise # lets just reraise it
