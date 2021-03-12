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
