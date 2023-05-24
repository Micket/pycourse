from question4 import SymmetricMatrix, Matrix, ABCDMatrix

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
