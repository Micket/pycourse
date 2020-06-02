
""" Question 2 """

import numpy as np
from scipy.integrate import odeint

## Part A

def derivative(y, t, beta, gamma, mu, N):

    """ Differential equation system for the SIRD-Model. """
    
    S, I, R, D = y

    dS_dt = - beta * I * S / N
    dI_dt = + beta * I * S / N - gamma * I - mu * I
    dR_dt = gamma * I
    dD_dt = mu * I

    dy_dt = [dS_dt, dI_dt, dR_dt, dD_dt]
    return dy_dt

## Part B

# -- Model parameters

N     = 1.e7
gamma = 1 / 7
mu    = 0.001 * gamma
R     = 1.5
beta  = gamma * R

# -- Initial condition

S_t0 = N
I_t0 = 10
R_t0 = 0
D_t0 = 0

y_t0 = [S_t0, I_t0, R_t0, D_t0]

# -- Time evolution

t = np.linspace(1, 365, num=365)
sol = odeint(derivative, y_t0, t, args=(beta, gamma, mu, N))
S, I, R, D = sol.T

## Part C

# -- Number of desceased per day

dD_dt = np.diff(D)

## Part D

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
subp = [2, 2, 1]
plt.subplot(*subp); subp[-1] += 1
plt.plot(t, S * 1e-6, label='$S$, Susceptible')
plt.plot(t, R * 1e-6, label='$R$, Recovered')
plt.xlabel('Time (days)')
plt.ylabel('$S$ susceptible, $R$ recovered\n (million people)')
plt.grid(True)
plt.legend(loc='best')

plt.subplot(*subp); subp[-1] += 1
plt.plot(t, D)
plt.xlabel('Time (days)')
plt.ylabel('$D$ desceased (people)')
plt.grid(True)

plt.subplot(*subp); subp[-1] += 1
plt.plot(t, I)
plt.xlabel('Time (days)')
plt.ylabel('$I$ Infectious (people)')
plt.grid(True)

plt.subplot(*subp); subp[-1] += 1
plt.plot(t[:-1], dD_dt)
plt.xlabel('Time (days)')
plt.ylabel('Daily number of desceased\n (people per day)')
plt.grid(True)

plt.tight_layout()
plt.savefig('figure_SIRDM_time_evolution.png', dpi=300)

plt.show()
