#!/usr/bin/env python

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from math import sin, cos, pi

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

def simulate_projectile(ang: float, c: float):
    params = [0.1, 9.82, c]  # m, g, c
    s0 = np.array([10 * cos(ang), 10 * sin(ang), 0, 0])
    t = np.arange(0, 2, 0.1)
    sol = integrate.odeint(time_derivative, s0, t, args=(params,))
    return sol

def plot_paths():
    # For computing the angles
    denominators = [3, 4, 5, 6]
    # Create the plot with 2x2 subplots
    fig, axs = plt.subplots(2, 2)  # axs is a 2x2 ndarray
    i = 0  # helper index
    for ax_s in axs:
        for ax in ax_s:
            denominator = denominators[i]
            alpha = pi/denominator
            i += 1
            for c in [0.0, 0.001, 0.002]:
                sol = simulate_projectile(alpha, c)
                # Extract x and y data from solution
                xs = [d[2] for d in sol]
                ys = [d[3] for d in sol]
                ax.plot(xs, ys, marker='.', label='c = {}'.format(c))
                ax.legend(title='α = π/{}'.format(denominator), loc='upper right')
                ax.set_xlabel('x [m]')
                ax.set_ylabel('y [m]')
                # Empirically derived limits
                ax.set_xlim([0, 17])
                ax.set_ylim([-9, 5])
    # Show the plot
    plt.subplots_adjust(wspace=0.3, hspace=0.3)
    plt.show()

if __name__ == "__main__":
    plot_paths()
