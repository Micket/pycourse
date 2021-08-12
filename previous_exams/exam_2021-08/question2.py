import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt

# Part A 1p
data = np.loadtxt('measurements.csv')
t_measurement = data[:,0]
y_measurement = data[:,1]

plt.plot(t_measurement, t_measurement, 'b')
plt.plot(t_measurement, y_measurement, 'r')
plt.plot(t_measurement, t_measurement**2, 'k')
plt.show()

# Part B 1p interpolate 
y_interp = scipy.interpolate.interp1d(t_measurement, y_measurement)
n = 1000
t = np.linspace(0, 1, n)
y = y_interp(t)

# Part C & D 3p
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
plt.show()

