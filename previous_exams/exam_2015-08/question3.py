class SparseMatrix:
    def __init__(self, I, J, V, nr, nc):
        # Copy the lists to not get owned later
        # Should probably sort these but whatever
        self.I = list(I)
        self.J = list(J)
        self.V = list(V)
        self.nr = nr
        self.nc = nc

    def get(self, row, col):

        if row >= self.nr or col >= self.nc:
            raise Exception("BoundsError")

        # Slow as a donger but whatever
        for rowz, colz, val in zip(self.I, self.J, self.V):
            if rowz == row and col == colz:
                return val

        return 0.0


    def transpose(self):
        return SparseMatrix(self.J, self.I, self.V,
                            self.nc, self.nr)

    def __mul__(self, vec):
        if type(vec) != list:
            raise NotImplemented
        if len(vec) != self.nc:
            raise Exception("DimensionError")

        output = [0 for _ in range(self.nr)]
        for row, col, val in zip(self.I, self.J, self.V):
            output[row] += val * vec[col]

        return output

    # Copy on multiplication?? What is this madness?
    def __rmul__(self, vec):
        return self.transpose() * vec



m = SparseMatrix([0, 3, 1, 2, 4, 0, 3], [0, 1, 2, 2, 3, 4, 4],
[3., 2., 4., 7., 9., 2., 4.], 5, 5)

# Check
mt = m.transpose()
for i in range(0, m.nr):
    for j in range(0, m.nc):
        if m.get(i, j) != mt.get(j, i):
            raise Exception("wtf bro")

v = [1.0, 0.0, 3.0, 2.0, 3.0]

print(m * v)
print(v * mt)