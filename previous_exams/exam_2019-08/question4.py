import abc
import copy

class BaseMatrix(metaclass=abc.ABCMeta):
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    @abc.abstractmethod
    def transpose(self):
        pass


class Matrix(BaseMatrix):
    def __init__(self, data):
        self.data = data
        super().__init__(len(self.data), len(self.data[0]))

    def __getitem__(self, pos):
        return self.data[pos[0]][pos[1]]

    def transpose(self):
        transposed_data = [[] for _ in range(self.columns)]
        for row in self.data:
            for i, value in enumerate(row):
                transposed_data[i].append(value)
        return Matrix(transposed_data)


class SymmetricMatrix(BaseMatrix):
    def __init__(self, data):
        self.data = data
        super().__init__(len(data), len(data))

    def transpose(self):
        return SymmetricMatrix(copy.deepcopy(self.data))

    def __getitem__(self, pos):
        if pos[0] <= pos[1]:
            return self.data[pos[0]][pos[1]-pos[0]]
        else:
            return self.data[pos[1]][pos[0]-pos[1]]


class ABCDMatrix(BaseMatrix):
    def __init__(self, a, b, c, d):
        super().__init__(a.rows + c.rows, a.columns + b.columns)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __getitem__(self, pos):
        if pos[0] < self.a.rows:
            if pos[1] < self.a.columns:
                return self.a[pos]
            else:
                return self.b[pos[0], pos[1] - self.a.columns]
        else:
            if pos[1] < self.c.columns:
                return self.c[pos[0] - self.a.rows, pos[1]]
            else:
                return self.d[pos[0] - self.a.rows, pos[1] - self.c.columns]

    def transpose(self):
        # [a, b]^T = [a^T, c^T]
        # [c, d]     [b^T, d^T]
        return ABCDMatrix(self.a.transpose(), self.c.transpose(),
                          self.b.transpose(), self.d.transpose())

# Denna får dom:
def print_matrix(m):
    for i in range(m.rows):
        for j in range(m.columns):
            print('{:>3}'.format(m[i, j]), end=' ')
        print('')

a = SymmetricMatrix([[1, 2, 3],[4, 5], [6]])
b = SymmetricMatrix([[7, 8, 9], [10, 11], [12]])
print_matrix(a)
#  1   2   3
#  2   4   5
#  3   5   6

c = Matrix([[13, 14, 15], [17, 18, 19]])
d = Matrix([[20, 21, 22],[23, 24, 25]])
print_matrix(d.transpose())
# 20  23
# 21  24
# 22  25

m = ABCDMatrix(a, b, c, d)
print_matrix(m)
#  1   2   3   7   8   9 
#  2   4   5   8  10  11 
#  3   5   6   9  11  12 
# 13  14  15  20  21  22 
# 17  18  19  23  24  25
 
mt = m.transpose()
print_matrix(mt)
#  1   2   3  13  17
#  2   4   5  14  18
#  3   5   6  15  19
#  7   8   9  20  23
#  8  10  11  21  24
#  9  11  12  22  25