#!/usr/bin/env python

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def time_derivative(s: np.ndarray, t: float, params):
    m, g, c = params
    v = s[0:2]  # velocity
    ev = - v / np.linalg.norm(v)  # (negative) direction of velocity
    fw = c / m * np.linalg.norm(v)**2 * ev  # wind force
    dsdt = [
        fw[0] / m,        # a_x
        - g + fw[1] / m,  # a_y
        s[0],             # v_x
        s[1]              # v_y
    ]
    return np.array(dsdt)

def simulate_projectile(c):
    params = [0.1, 9.82, c]  # m, g, c
    s0 = np.array([10, 10, 0, 0])
    t = np.arange(0, 2, 0.1)
    sol = integrate.odeint(time_derivative, s0, t, args=(params,))
    return sol

def plot_paths():
    fig, ax = plt.subplots()
    # Create the plot
    ax.axis('equal')
    plt.title('Flight path')
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    # Solve for different c and plot datapoints
    for c in [0.0, 0.001, 0.002]:
        sol = simulate_projectile(c)
        # Extract x and y data from solution
        xs = [d[2] for d in sol]
        ys = [d[3] for d in sol]
        plt.plot(xs, ys, marker='.', label='c = ' + str(c))
    plt.legend()
    # Show the plot
    plt.show()

if __name__ == "__main__":
    plot_paths()

