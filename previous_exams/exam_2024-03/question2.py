import math
import numpy
import scipy.integrate
import time


def f(x):
    return math.cos(x) - math.sin(x**2)

# Part D
N = 10000000
x_span = (0, 5)
x = numpy.linspace(x_span[0], x_span[1], N)


time1 = time.time()

# Part A
x = numpy.linspace(x_span[0], x_span[1], N)
f_x = numpy.zeros(N)
for i in range(len(x)):
    f_x[i] = f(x[i])
val1 = scipy.integrate.trapz(f_x, x)


time2 = time.time()

# Part B
x = numpy.linspace(x_span[0], x_span[1], N)
f_x = numpy.cos(x) - numpy.sin(x**2)
val2 = scipy.integrate.trapz(f_x, x)



time3 = time.time()

# Part C
val3, err = scipy.integrate.quad(f, x_span[0], x_span[1])

time4 = time.time()

print(f"N = {N}")
print(f"loop  = {time2 - time1:e}, {val1}")
print(f"numpy = {time3 - time2:e}, {val2}")
print(f"quad  = {time4 - time3:e}, {val3}, {err}")

#########################

# Output:
"""
N = 100000
loop  = 3.051353e-02, -1.486841557693728
numpy = 1.663685e-03, -1.486841557693728
quad  = 4.529953e-05, -1.486841555828461, 1.9324843574322625e-09

N = 1000000
loop  = 3.088174e-01, -1.4868415558471133
numpy = 1.574659e-02, -1.4868415558471133
quad  = 6.699562e-05, -1.486841555828461, 1.9324843574322625e-09

N = 10000000
loop  = 2.966166e+00, -1.4868415558286496
numpy = 1.921186e-01, -1.4868415558286496
quad  = 6.651878e-05, -1.486841555828461, 1.9324843574322625e-09
"""
