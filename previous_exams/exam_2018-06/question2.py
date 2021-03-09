import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def f(x):
    return (x-1)**2 + 10*np.sin(x)

x = np.arange(-10, 10, 0.1)

methods = ['CG', 'BFGS', 'Powell']
starts = [1, 5, 7, 10]

for i, method in enumerate(methods):
    plt.subplot(2,2,i+1)
    plt.plot(x, f(x))
    plt.xlabel('$x$')
    plt.ylabel('$f(x)$')
    plt.title(method)
    plt.grid()

    print('Using method:', method)

    for start in starts:
        res = optimize.minimize(f, start, method=method, options={'disp': False})
        plt.plot(res.x, f(res.x), 'bo')
        print(' Start guess of', start, 'found x of', res.x, 'with function value', f(res.x))

print('Global optimization')
res = optimize.basinhopping(f, 0, disp=False)
print(' Start guess of', 0, 'found x of', res.x, 'with function value', f(res.x))

plt.subplot(2,2,4)
plt.plot(x, f(x))
plt.title('Global and roots')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.grid()
plt.plot(res.x, f(res.x), 'bo')


for start in [0, -3]:
    root = optimize.fsolve(f, start)
    plt.plot(root, f(root), 'rx')
    print ('Starting at x=', start, ', found root at x=', root, 'with function value', f(root))

plt.show()

