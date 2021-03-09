import numpy as np

from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigs

data = np.loadtxt("matrix.csv", delimiter=",", skiprows=1)

rows = data[:, 0]
cols = data[:, 1]
vals = data[:, 2]

S = csr_matrix((vals, (rows, cols)))
eig_val, eig_vec = eigs(S, k=1)

print(eig_val)