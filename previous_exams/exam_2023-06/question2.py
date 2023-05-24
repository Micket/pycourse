import numpy as np

# Read data into "a", print "a"
a = np.loadtxt("values.txt", dtype=np.int)
print('a = ', a)

# create "b" by reshaping "a" into 2 blocks, 4 rows and 3 columns
b = a.reshape((2, 4, 3))
print('b =\n', b)

# Print block 0, print row 2, print column 1
print('block 0:\n', b[0, :, :])
print('row 2:\n', b[:, 2, :])
print('column 1:\n', b[:, :, 1])

# Print block 1 with rows reversed
print('block 1, rows reversed:\n', b[1, ::-1, :])

# Make a mask "c, d, e" for all values < 50, 50 < 75, >= 75, print them
c = b < 50
d = (b >= 50) & (b < 75)
e = b >= 75

print('c =\n', c)
print('d =\n', d)
print('e =\n', e)

# Print the values
print('< 50:\n', b[c])
print('>=50 and < 75:\n', b[d])
print('>= 75:\n', b[e])

# Find row (axis 1) with highest sum for each block
rowsum = b.sum(axis=2)
print('row-sums:\n', rowsum)
maxrow = rowsum.argmax(axis=1)
print('index of max:', maxrow)

print('Row with highest sum in block 0:', b[0, maxrow[0], :])
print('Row with highest sum in block 1:', b[1, maxrow[1], :])

