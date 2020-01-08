def debug_print_matrix(m):
    for i in range(m.rows):
        for j in range(m.cols):
            print('{:2}'.format(m[i, j]), end=' ')
        print()


dense = DenseMatrix([[1,2,3,4,5],
                     [5,4,3,2,1],
                     [0,0,0,0,0],
                     [1,1,1,1,1],
                     [1,0,1,0,1]])

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
