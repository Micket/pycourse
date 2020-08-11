
import numpy as np

# -- Part A

def new_rotated_points(A, N_p, r):    
    dA = 1.j * r * np.exp(1.j * 2*np.pi/N_p * np.arange(N_p))
    A_new = (A[:, None] + dA[None, :]).flatten()
    return A_new


# -- Test Part A

np.set_printoptions(precision=2, floatmode='fixed', suppress=True, linewidth=1000)

for N_p in [2, 4, 6]:
    A = new_rotated_points(np.array([0.]), N_p=N_p, r=0.5)
    print(f'N_p = {N_p} : A = {A}')


# -- Part B
    
def make_points(N_p=5, N_iter=3, r=0.5):
    A = np.array([0.])
    for m in range(N_iter):
        A = new_rotated_points(A, N_p, r**m)
    x, y = A.view(np.float).reshape((len(A), 2)).T
    return x, y


# -- Test Part B

print('{0}\n{1}'.format(*make_points(N_p=4, N_iter=2, r=0.5)))


# -- Part C

import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

plt.figure(figsize=(5, 5))
ax = plt.subplot()

x, y = make_points(N_p=5, N_iter=3, r=0.5)
voronoi_plot_2d(Voronoi(np.vstack((x,y)).T), ax=ax)

plt.axis('square')
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.axis(False)
plt.tight_layout()

plt.savefig('figure_point_set.png', dpi=600)
plt.show()

