import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

n = 20
r = 0.03

t_rand = np.concatenate(([0], np.random.rand(n-2)*r, [0]))
y_rand = np.concatenate(([0], np.random.rand(n-2)*r, [0]))

t = (np.linspace(0, 1, n) + t_rand)**2 # Just make it non-uniform
y = t**1.7 + y_rand*t

plt.plot(t, y, 'x')
plt.show()
np.savetxt('measurements.csv', np.transpose([t,y]))

