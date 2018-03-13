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

