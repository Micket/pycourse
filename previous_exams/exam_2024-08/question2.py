import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate

# Part A
data = np.loadtxt('measurements.txt')
t_measurement = data[:,0]
y_measurement = data[:,1]

plt.plot(t_measurement, y_measurement, 'r')
plt.plot(t_measurement, t_measurement, 'b')     # f(t) = t
plt.plot(t_measurement, t_measurement**2, 'k')  # f(t) = t^2
plt.legend(['measurments', 'f(t) = t', 'f(t) = t^2'], loc='best')
plt.grid()
plt.show()

# Part B
y_interp = scipy.interpolate.interp1d(t_measurement, y_measurement)
n = 1000
t = np.linspace(0, 1, n)
y = y_interp(t)

# Part C
best_error, c_best = 1, 1  # Set initial values (very large error)
for c in np.linspace(1, 2, 11):
    z = t**c
    error = np.linalg.norm(z - y)/(n-1)
    print(f'{c:.2f} -> {error}')
    if error < best_error:
        best_error, c_best = error, c

print(f'Lowest error obtained with c={c_best}')
plt.plot(t_measurement, y_measurement, 'r')
plt.plot(t, t**c_best, 'k')
plt.legend(['measurments', f'f(t) = t^{c_best:3.1f}'], loc='best')
plt.grid()
plt.show()

