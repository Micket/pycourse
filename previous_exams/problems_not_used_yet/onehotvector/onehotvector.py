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
        if item < 0 or item >= length:
            raise IndexError("out of bounds")
        return 1 if item == self.index else 0

    def __mul__(self, matrix):
        if matrix.shape[1] == self.length:
            raise IndexError("Incompatible matrix size")

        return matrix[:, self.index]

    def __rmul__(self, matrix):
        if matrix.shape[0] == self.length:
            raise IndexError("Incompatible matrix size")

        return matrix[self.index, :]

    def toarray(self):
        x = np.zeros(self.length)
        x[self.index] = 1
        return x
