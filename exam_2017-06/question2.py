import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

# A: Read data
xy = np.loadtxt("values.txt", dtype=np.float)
x = xy[:, 0]
y = xy[:, 1]


# B Splines
x_eval = np.linspace(np.min(x), np.max(x), num=300) # Construct x-points for spline/poly evaluation

plt.subplot(2,1,1)
plt.plot(x, y, 'x')
leg = ['Data']
for smooth in [None, 0, 15]:
    spline = UnivariateSpline(x, y, s=smooth, k=2)
    y_spline = spline(x_eval)
    plt.plot(x_eval, y_spline)
    leg.append('Spline smoothing = ' + str(smooth))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Splines')
plt.legend(leg, loc='best')


# C Polynoms
def funk (x, A, B, C=0, D=0, E=0):
    return A + B * x + C * x * x + D * np.power (x, 3) + E * np.power(x,4)

plt.subplot(2, 1, 2)
plt.plot(x, y, 'x')
leg = ['Data']
for order in range(2, 5):
    params = np.polyfit(x,y, order)[::-1]
    print('Fit parameters: ', params)
    plt.plot(x_eval, funk(x_eval, *params))
    leg.append('Poly order ' + str(order))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynoms')
plt.legend(leg, loc='best')

plt.show()
