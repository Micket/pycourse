f = -Sine() + Constant(5.7) + Polynomial(2,3)  # f(x) = -sin(x) + 5.7 + 2*x**3
print("f(1.5)  =", f(1.5))
df = f.derivative() # f'(x) = cos(x) + 6*x**2
print("f'(1.5) =", df(1.5))

g = Sum([Sine(), Negate(Cosine()), Constant(1)]) # g(x) = sin(x) - cos(x) + 1
print("g(0.3)  =", g(0.3))
dg = g.derivative() # g'(x) = cos(x) + sin(x)
print("g'(0.3) =", dg(0.3))

h = ((-f) + g).derivative()  # h(x) = - 6*x**2 + sin(x)
print("h(3.2)  =", h(3.2))
