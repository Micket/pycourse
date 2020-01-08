import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


# A: Read data
xy = np.loadtxt("values.txt", dtype=np.float)
x = xy[:, 0]
y1 = xy[:, 1]
y2 = xy[:, 2]


# B/C Polynoms and plot
x_eval = np.linspace(np.min(x), np.max(x), num=500) # Construct x-points for poly evaluation

plt.plot(x, y1, 'r.', x, y2, 'g.')
leg = ['y1', 'y2']

def funk (x, A, B, C=0):
    return A + B * x + C * x * x

p1 = dict()
p2 = dict()
for order in range(1, 3):
    p1[order] = np.polyfit(x,y1, order)[::-1]
    print('Fit y1(o={}): {}'.format(order, p1[order]))
    plt.plot(x_eval, funk(x_eval, *p1[order]))
    leg.append('y1 order ' + str(order))

    p2[order] = np.polyfit(x,y2, order)[::-1]
    print('Fit y2(o={}): {}'.format(order, p2[order]))
    plt.plot(x_eval, funk(x_eval, *p2[order]))

    leg.append('y2 order ' + str(order))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Customer satisfaction')
plt.legend(leg, loc='best')

def f_err (x, p1, p2):
    return funk(x, *p1) - funk(x, *p2)

# D Root(s)
start = 4
o1 = 2
o2 = 2
x_root = dict()
for o2 in [1,2]:
    root = optimize.fsolve(f_err, start, args=(p1[o1], p2[o2]))
    print('Root at:', root, ' for orders:', o1, o2)
    x_root[o2] = root[0]
    plt.plot(x_root[o2], funk(x_root[o2], *p2[o2]), 'ko', MarkerSize=10)

plt.show()


