# coding=utf-8

import numpy as np
import scipy.sparse as sp
from time import time

PRINT = False
MULTI = 10

types = [{'name': 'NumPy ndarray', 'create': np.zeros},
         {'name': 'SciPy sparse Lil', 'create': sp.lil_matrix},
         {'name': 'SciPy sparse CSC', 'create':  sp.csc_matrix},
         {'name': 'SciPy sparse CSR', 'create': sp.csr_matrix},
         {'name': 'SciPy sparse DOK', 'create': sp.dok_matrix}]


def assemble_matrix(A, ij, v):

    start_time = time()

    for indices, value in zip(ij, v):
        i = indices[0]
        j = indices[1]
        A[i, j] += value

    print("\tAssemble time: ", time() - start_time)


def multiply_matrix(A, rounds):

    start_time = time()

    for i in range(rounds):
        B = A * A

    print("\tMultiply time: ", time() - start_time)


ij = np.loadtxt("large.txt", usecols=[0, 1], dtype=np.int)
v = np.loadtxt("large.txt", usecols=[2], dtype=np.float)
if PRINT: print(ij, v)

N = np.amax(ij) + 1
print('Read matrix size: ', N)

for tp in types:
    print(tp['name'])
    start_time = time()
    A = tp['create']((N, N), dtype=np.float)
    assemble_matrix(A, ij, v)
    multiply_matrix(A, MULTI)
    print("\tFull time    : ", time() - start_time)
    if PRINT: print(A)

# Assemble in Lil, convert to CSR and multiply
print('SciPy sparse Lil -> CSR')
start_time = time()
A = sp.lil_matrix((N, N), dtype=np.float)
assemble_matrix(A, ij, v)
A = A.tocsr()
multiply_matrix(A, MULTI)
print("\tFull time    : ", time() - start_time)
if PRINT: print(A)
