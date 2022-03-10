import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

# A: Read data
xy = np.loadtxt("values.txt", dtype=float)
x = xy[:, 0]
y = xy[:, 1]


# B Splines
x_eval = np.linspace(np.min(x), np.max(x), num=300) # Construct x-points for spline/poly evaluation

plt.subplot(2,1,1)
plt.plot(x, y, 'x')
legend = ['Data']
for smooth in [None, 0, 15]:
    spline = UnivariateSpline(x, y, s=smooth, k=2)
    y_spline = spline(x_eval)
    plt.plot(x_eval, y_spline)
    legend.append('Spline smoothing = ' + str(smooth))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Splines')
plt.grid()
plt.legend(legend, loc='best')
# Smoothing 15 seems the best


# C Polynoms
def polyfunk (x, C0, C1, C2=0, C3=0, C4=0, C5=0):
    return C0 + C1 * x + C2 * x * x + C3 * np.power (x, 3) + C4 * np.power(x, 4) + C5 * np.power(x, 5)

plt.subplot(2, 1, 2)
plt.plot(x, y, 'x')
legend = ['Data']
for order in range(2, 6):
    params = np.polyfit(x, y, order)[::-1]
    print(f'Polynom order {order} paramaters: ', end='')
    for i, param in enumerate(params):
        print(f'C{i} = {param}', end=', ')
    print()
    plt.plot(x_eval, polyfunk(x_eval, *params))
    legend.append(f'Order {order} polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynoms')
plt.grid()
plt.legend(legend, loc='best')
# Order 4 seems sufficient

plt.show()
