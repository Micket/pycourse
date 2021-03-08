# 1. Create class for FourierSerie (neglect phase?)
# 2. Make is call'able (or a separate evaluate-method?)
# 3. Add support for * and *= between a FourierSerie and a scalar
# 4. Add a static method "__add_coefficients" that adds 2 vectors, padding length with zeroes. Use it to add support for + and +=

from math import cos, pi
import numpy as np

class FourierSerie:
    def __init__(self, coef):
        self.coef = coef

    @staticmethod
    def __add_coefficients(coef_a, coef_b):
        max_len = max(len(coef_a), len(coef_b))
        c = [a*b for a, b in zip(coef_a, coef_b)]
        c += coef_a[max_len:] + coef_b[max_len:]

    def __add__(self, other):
        return FourierSerie(self.__add_coefficients(self.coef + other.coef))

    def __iadd__(self, other):
        self.coef = self.__add_coefficients(self.coef, other.coef)
        return self

    def __imul__(self, s):
        self.coef = [s * c for c in self.coef]
        return self

    def __mul__(self, s):
        return FourierSerie([s * c for c in self.coef])

    def __iter__(self):
        for i, c in enumerate(self.coef):
            yield lambda x: c*cos(2*pi*i*x)

    def __call__(self, x):
        s = 0.
        for f in self:
            s += f(x)
        return s


a = FourierSerie([0., 2., 3.])
b = FourierSerie([4., 6.])
c = a + b

for f in c:
    print(f(0.7))

print(c(0.7))

d = FourierSerie([1.])
print(d(1.))
