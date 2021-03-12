from math import cos, pi

class CosineSerie:
    def __init__(self, coef):
        self.coef = coef

    def __repr__(self):
        return f"CosineSerie({self.coef})"

    @staticmethod
    def __add_coefficients(coef_a, coef_b):
        min_len = min(len(coef_a), len(coef_b))
        c = [a+b for a, b in zip(coef_a, coef_b)]
        c += coef_a[min_len:] + coef_b[min_len:]
        return c

    def __add__(self, other):
        return CosineSerie(self.__add_coefficients(self.coef, other.coef))

    def __iadd__(self, other):
        self.coef = self.__add_coefficients(self.coef, other.coef)
        return self

    def __iter__(self):
        return iter(self.coef)

    def __len__(self):
        return len(self.coef)

    def evaluate_term(self, i, x):
        if i < 0:
            raise IndexError(f"Negative index")
        if i >= len(self.coef):
            return 0.
        return self.coef[i]*cos(2*pi*i*x)

    def __call__(self, x):
        s = 0.
        for i, c in enumerate(self):
            s += c*cos(2*pi*i*x)
        return s

a = CosineSerie([1., 2., 3.])
b = CosineSerie([4., 6.])

print("a(0.5) =", a(0.5))
print("repr(b) =", repr(b))

c = CosineSerie([2., 2.])
c += a
d = b + CosineSerie([1., 1., 1., 1.])

print("c.evaluate_term(0, 0.5) =", c.evaluate_term(0, 0.5))
print("c.evaluate_term(1, 0.5) =", c.evaluate_term(1, 0.5))
print("c.evaluate_term(2, 0.5) =", c.evaluate_term(2, 0.5))
assert c.evaluate_term(3, 0.5) == 0
assert c.evaluate_term(4, 0.5) == 0
try:
    c.evaluate_term(-1, 0.5)
except IndexError as e:
    print('IndexError:', e)

print(f"d has {len(d)} non-zero coefficients")
print("Coefficients of d:", end=' ')
for coefficient in d:
    print(coefficient, end=' ')
print()
