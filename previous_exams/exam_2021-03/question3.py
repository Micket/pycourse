from math import cos, pi

class CosineSerie:
    def __init__(self, coef):
        self.coef = coef

    def __repr__(self):
        return f"CosineSerie({self.coef})"

    @staticmethod
    def __add_coefficients(coef_a, coef_b):
        max_len = max(len(coef_a), len(coef_b))
        c = [a*b for a, b in zip(coef_a, coef_b)]
        c += coef_a[max_len:] + coef_b[max_len:]
        return c

    def __add__(self, other):
        return CosineSerie(self.__add_coefficients(self.coef, other.coef))

    def __iadd__(self, other):
        self.coef = self.__add_coefficients(self.coef, other.coef)
        return self

    def __imul__(self, s):
        self.coef = [s * c for c in self.coef]
        return self

    def __mul__(self, s):
        return CosineSerie([s * c for c in self.coef])

    def __iter__(self):
        return iter(self.coef)

    def __len__(self):
        return len(self.coef)

    def evaluate_term(self, i, x):
        if i < 0:
            raise IndexError(f"Outside of range")
        if i >= len(self.coef):
            return 0.
        return self.coef[i]*cos(2*pi*i*x)

    def __call__(self, x):
        s = 0.
        for i, c in enumerate(self):
            s += c*cos(2*pi*i*x)
        return s

f = CosineSerie([3., 2., 1.])
print(f(0.5))

a = CosineSerie([1., 2., 3.])
a *= 2.
b = a * 3.
c = CosineSerie([4., 6.])
c += a
d = a + CosineSerie([1., 1., 1., 1.])

print("a(0.5) =", a(0.5))
print("repr(b) =", repr(b))

print("c.evaluate_term(0, 0.5) =", c.evaluate_term(0, 0.5))
print("c.evaluate_term(1, 0.5) =", c.evaluate_term(1, 0.5))
assert c.evaluate_term(4, 0.5) == 0

print("d has {len(d)} non-zero coefficients")
print("Coefficients of d:", end=' ')
for coefficient in d:
    print(coefficient, end=' ')
print()
