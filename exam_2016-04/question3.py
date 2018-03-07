import numpy as np


class Diagonal:
    def __init__(self, mat):
        # Part B:
        if mat.shape[0] != mat.shape[1]:
            raise ValueError("Matrix is not square")
        self.mat = mat

    def __iter__(self):
        class DiagonalIt:
            def __init__(self, mat):
                self.mat = mat
                self.it = iter(range(len(mat)))

            def __next__(self):
                v = next(self.it)
                return self.mat[v, v]

        return DiagonalIt(self.mat)

# Testing it out:
my_matrix = np.array([[1,2,3,4,5],[1,4,3,2,4],[5,4,2,3,3],[1,1,1,1,1],[2,0,0,3,0]])
s = 0
d = Diagonal(my_matrix)
for x in d:
    s += x
print(s)
print(list(d))

my_matrix = np.random.rand(5, 4)
try:
    for d in Diagonal(my_matrix):
        print(d)
except ValueError as e:
    print("Oh no: ", e)
