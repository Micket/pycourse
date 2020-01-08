import abc

class Matrix(metaclass=abc.ABCMeta):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    @abc.abstractmethod
    def transpose(self):
        pass

    @abc.abstractmethod
    def __getitem__(self):
        pass


class DenseMatrix(Matrix):
    def __init__(self, values, transposed=False):
        self.values = values
        self.transposed = transposed
        if self.transposed:
            super().__init__(len(self.values[0]), len(self.values))
        else:
            super().__init__(len(self.values), len(self.values[0]))

    def transpose(self):
        return DenseMatrix(self.values, not self.transposed)

    def __getitem__(self, pos):
        if self.transposed:
            pos = pos[::-1]
        return self.values[pos[0]][pos[1]]


class SymmetricMatrix(Matrix):
    def transpose(self):
        return self


class BandedMatrix(SymmetricMatrix):
    def __init__(self, band_values):
        self.band_values = band_values
        self.width = len(self.band_values[0])
        n = len(self.band_values)
        super().__init__(n, n)

    def __getitem__(self, pos):
        row, col = sorted(pos)
        offset = col - row
        if offset >= self.width:
            return 0
        else:
            return self.band_values[row][offset]


# Test code (given):
def debug_print_matrix(m):
    for i in range(m.rows):
        for j in range(m.cols):
            print('{:2}'.format(m[i, j]), end=' ')
        print()


dense = DenseMatrix([[1,2,3,4,5],
                     [5,4,3,2,1],
                     [0,0,0,0,0],
                     [1,1,1,1,1]])

print('Dense matrix:')
debug_print_matrix(dense)
print('Dense matrix transpose:')
debug_print_matrix(dense.transpose())

banded = BandedMatrix([[1,2,3],
                       [4,5,6],
                       [7,8,9],
                       [10,11,12],
                       [13,14],
                       [15]])

print('Banded matrix:')
debug_print_matrix(banded)
print('Banded matrix transpose:')
debug_print_matrix(banded.transpose())
