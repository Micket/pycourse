import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

C_in = 2.5
V = 100
k = 0.15
F = lambda t: 20.1
C0 = 0.5

def dC_dt(C, t):
    return F(t)/V * (C_in - C) - k*C*C

t = np.linspace(0, 10, 1001)
C = odeint(dC_dt, C0, t)[:,0]

# Many options
ind = np.where(C >= 1.0)[0][0]

print('t = {:.1f}, C = {:e}'.format(t[ind], t[ind]))

Cp = dC_dt(C, t)
mask = Cp < 0.01
t2 = t[mask][0]
C2 = C[mask][0]
print('t = {:.1f}, C = {:e}, dC/dt = {:e}'.format(t2, C2, dC_dt(C2, t2)))


plt.plot(t, C, t, Cp)
plt.show()
