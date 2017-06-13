from math import sqrt, cos, sin, atan2

class Complex(object):
    def __init__(self, re, im = 0):
        self.re = re
        self.im = im

    def real(self):
        return self.re

    def imag(self):
        return self.im

    def __str__(self):
        return str(self.re) + (" - " if self.im < 0 else " + ") + str(abs(self.im)) + "im"

    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

    def __lt__(self, other):
        raise(UnorderedException)

    def __add__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)
        return Complex(self.re + other.re, self.im + other.im)

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)
        a, b = self.real(), self.imag()
        c, d = other.real(), other.imag()
        return Complex(a*c - b*d, a*d + b*c)

    def __rmul__(self, other):
        return self * other

    def __abs__(self):
        return sqrt(self.real()**2 + self.imag()**2)

    def topolar(self):
        return abs(self), atan2(self.imag(), self.real())

    @staticmethod
    def frompolar(r, theta):
        return Complex(r * cos(theta), r * sin(theta))


class UnorderedException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Complex numbers are unordered"

im = Complex(0, 1)
