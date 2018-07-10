import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
​
C_in = 5.5
V = 100
k = 0.18
F = lambda t: 17.3
C0 = 0.3
​
def dC_dt(C, t):
    return F(t)/V * (C_in - C) - k*C*C
​
t = np.linspace(0, 10, 10001)
C = odeint(dC_dt, C0, t)[:,0]
​
# Many options
ind = np.where(C >= 1.0)[0][0]
​
print('t = {:.2f}, C = {:e}'.format(t[ind], C[ind]))
​
Cp = dC_dt(C, t)
mask = Cp < 0.01
t2 = t[mask][0]
C2 = C[mask][0]
print('t = {:.2f}, C = {:e}, dC/dt = {:e}'.format(t2, C2, dC_dt(C2, t2)))
​
plt.plot(t, C, t, Cp)
plt.show()
