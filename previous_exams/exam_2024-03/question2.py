import numpy
import time
import scipy.integrate
import math as m


def f(x):
    return m.cos(x) - m.sin(x**2)

# Part D
n = 10000000
x_span = (0, 5)
x = numpy.linspace(x_span[0], x_span[1], n)


time1 = time.time()

# Part A
x = numpy.linspace(x_span[0], x_span[1], n)
f_x = numpy.zeros(n)
for i in range(len(x)):
    f_x[i] = f(x[i])
val1 = scipy.integrate.trapz(f_x, x)


time2 = time.time()


# Part B
x = numpy.linspace(x_span[0], x_span[1], n)
f_x = numpy.cos(x) - numpy.sin(x**2)
val2 = scipy.integrate.trapz(f_x, x)



time3 = time.time()


# Part C
val3, err = scipy.integrate.quad(f, x_span[0], x_span[1])

time4 = time.time()


print("loop  = {:e}, {}".format(time2 - time1, val1))
print("numpy = {:e}, {}".format(time3 - time2, val2))
print("quad  = {:e}, {}, {}".format(time4 - time3, val3, err))

#########################

# Output:
"""
loop  = 7.192037e-01, -1.4868415558471133
numpy = 6.695676e-02, -1.4868415558471133
quad  = 1.788139e-04, -1.486841555828461, 1.9324843574322625e-09

loop  = 6.175759e+00, -1.4868415558286496
numpy = 7.587125e-01, -1.4868415558286496
quad  = 1.540184e-04, -1.486841555828461, 1.9324843574322625e-09
"""