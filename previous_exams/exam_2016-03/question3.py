# This solution example has a lot of code, since it includes very rigorous bounds checking.

class Matrix:
    def __init__(self, nr, nc):
        self.nr = nr
        self.nc = nc

    def bounds_check(self, item):
        if item[0] >= self.nr or item[1] >= self.nc:
            raise IndexError("Index out of range: ({},{})".format(*item))
        if item[0] < 0 or item[1] < 0:
            raise IndexError("Negative index not supported: ({},{})".format(*item))


class IdentityMatrix(Matrix):
    def __init__(self, size):
        super().__init__(size, size)

    # Part B:
    def __str__(self):
        return "Identity matrix, size: {}x{}".format(self.nr, self.nc)

    # Part C:
    def __getitem__(self, item):
        self.bounds_check(item)
        return 1 if item[0] == item[1] else 0

    # Part C:
    def __setitem__(self, item):
        raise NotImplementedError("Identities are immutable")

    # Part D:
    def __mul__(self, val):
        if type(val) == float or type(val) == int:
            return DiagonalMatrix([val]*self.nr)
        elif type(val) == list:
            return val.copy()
        else:
            raise TypeError("Unsupported type: {}".format(type(val)))

    def __rmul__(self, val):
        return self.__mul__(val)


class DiagonalMatrix(Matrix):
    def __init__(self, diag):
        super().__init__(len(diag), len(diag))
        self.diag = diag

    # Part B:
    def __str__(self):
        s = "Diagonal matrix, size: {}x{}\nDiagonal: [".format(self.nr, self.nc)
        # Fancy printing:
        v = [str(x) for x in self.diag]
        if len(self.diag) <= 10:
            s += ', '.join(v)
        else:
            s += ', '.join(v[:3]) + ' ... '+ ', '.join(v[-3:])
        return s + ']'

    # Part C:
    def __getitem__(self, item):
        self.bounds_check(item)
        return self.diag[item[0]] if item[0] == item[1] else 0

    # Part C:
    def __setitem__(self, item, val):
        self.bounds_check(item)
        if item[0] != item[1]:
            raise IndexError("Diagonal matrix only support setting diagonal values ({},{})".format(*item))
        self.diag[item[0]] = val

    # Part D:
    def __mul__(self, val):
        if type(val) == float or type(val) == int:
            return DiagonalMatrix([d * val for d in self.diag])
        elif type(val) == list:
            # Bonus check:
            if len(self.diag) != self.nr:
                raise ValueError('List not of correct size; {} should be {}'.format(len(val), self.nr))
            return [x*y for x, y in zip(self.diag, val)]
        else:
            raise TypeError("Unsupported type: {}".format(type(val)))

    def __rmul__(self, val):
        return self.__mul__(val)


class DenseMatrix(Matrix):
    def __init__(self, values):
        super().__init__(len(values), len(values[0]))
        self.values = values
        # Part E:
        for i, row in enumerate(values):
            if len(row) != self.nc:
                raise MatrixSizeError(i, len(row), self.nc)

    # Part B:
    def __str__(self):
        s = "Dense matrix, size: {}x{}\n".format(self.nr, self.nc)
        # Medium fancy printing:
        for r in range(min(5, self.nr)):
            s += '['
            s += ', '.join([str(x) for x in self.values[r][:5]])
            if self.nc > 5:
                s += ', ...'
            s += "]\n"
        if self.nr > 5:
            s += '[...]\n'

        return s

    # Part C:
    def __getitem__(self, item):
        self.bounds_check(item)
        return self.values[item[0]][item[1]]

    # Part C:
    def __setitem__(self, item, val):
        self.bounds_check(item)
        self.values[item[0]][item[1]] = val

    def __mul__(self, val):
        if type(val) == float or type(val) == int:
            return DenseMatrix([[x * val for x in row] for row in self.values])
        elif type(val) == list:
            # Dot product reminder: y[i] = A_[i,j] * x_[j] !
            res = [[0.]*self.nc for x in range(self.nr)]
            for i in range(self.nr):
                for j in range(self.nc):
                    res[i][j] += self.values[i][j] * val[j]
            return res
        else:
            raise TypeError("Unsupported type: {}".format(type(val)))

    def __rmul__(self, val):
        # Copy paste is good enough for the exam! Identical to __mul__ but we switch the index
        if type(val) == float or type(val) == int:
            return DenseMatrix([[x * val for x in row] for row in self.values])
        elif type(val) == list:
            # Dot product reminder: y[i] = A_[i,j] * x_[j] !
            val = [[0.]*self.nc for x in range(self.nr)]
            for i in range(self.nr):
                for j in range(self.nc):
                    val[i][j] += self.values[j][i] * val[j]
            return val
        else:
            raise TypeError("Unsupported type: {}".format(type(val)))


# Part E:
class MatrixSizeError(Exception):
    def __init__(self, i, rowlen, ncol):
        self.i = i
        self.rowlen = rowlen
        self.ncol = ncol

    def __str__(self):
        return "Row number {} has {} columns, but should have {}.".format(self.i, self.rowlen, self.ncol)


# Note: You wouldn't have to do this extensive testing in order to achieve full points.
# It is included here to illustrate and teach how these things work.

# Test creation:
a = IdentityMatrix(3)
b1 = DiagonalMatrix([2.0, 3.5, 2.2, 2.2, 7.0])
b2 = DiagonalMatrix([2.0, 3.5, 2.2, 5.3, 4.3, 12.0, 2.2, 9.3, 1.2, 2.3, 2.2, 7.0])
c1 = DenseMatrix([[2.0, 0.0, 1.4],
                [0.5, 1.0, 1.0],
                [0.8, 3.0, 0.0]])

c2 = DenseMatrix([[2.0, 0.0, 1.4, 1, 2, 3, 4],
                [0.5, 1.0, 1.0, 1, 2, 3, 4],
                [0.8, 3.0, 0.0, 1, 2, 3, 4]])

c3 = DenseMatrix([[2.0, 0.0, 1.4],
                [0.5, 1.0, 1.0],
                [0.8, 3.0, 0.0],
                [0.8, 3.0, 0.0],
                [0.8, 3.0, 0.0],
                [0.8, 3.0, 0.0]])

# Test print:
print('a:', a)
print('b1:', b1)
print('b2:', b2)
print('c1:', c1)
print('c2:', c2)
print('c3:', c3)

# Test get-index:
print(a[2, 2], b1[2, 2], c1[2, 2])
print(a[1, 2], b1[1, 2], c1[1, 2])
# Test bounds checking
try:
    print(a[10,2])
except IndexError as e:
    print(e)

# Test a bit of set-index
b1[2, 2] = 3.14
c1[1, 2] = 3.14
print(b1)
print(c1)

# Test scaling.
print("a * 3 =", a * 1.5)
print("3 * b1 =", 1.5 * b1)
print("3 * c1 =", 1.5 * c1)
# Test dot product
print("a * x =", a * [1, 2, 3])
print("x * b1 =", [1, 2, 3] * b1)
print("c1 * x =", c1 * [1, 2, 3])
try:
    print(c1 * "Hello")
except:
    print("Didn't work")


# Test the exception
try:
    m = DenseMatrix([[1,2,3],[4,5,6],[7,8],[9,10,11]])
except MatrixSizeError as e:
    print("You better fix row {}!".format(e.i))
    print(e)
