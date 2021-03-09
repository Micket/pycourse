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
