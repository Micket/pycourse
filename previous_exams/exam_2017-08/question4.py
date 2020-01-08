import abc, math

class Function(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def derivative(self):
        pass

    def __neg__(self):
        return Negate(self)

    def __add__(self, other):
        return Sum([self, other])


class Negate(Function):
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, x):
        return -self.fun(x)

    def derivative(self):
        return Negate(self.fun.derivative())


class Sum(Function):
    def __init__(self, funs):
        self.funs = funs

    def __call__(self, x):
        return sum([fun(x) for fun in self.funs])

    def derivative(self):
        return Sum([fun.derivative() for fun in self.funs])


class Sine(Function):
    def __call__(self, x):
        return math.sin(x)

    def derivative(self):
        return Cosine()


class Cosine(Function):
    def __call__(self, x):
        return math.cos(x)

    def derivative(self):
        return -Sine()


class Constant(Function):
    def __init__(self, value):
        self.value = value

    def __call__(self, x):
        return self.value

    def derivative(self):
        return Constant(0)


class Polynomial(Function):
    def __init__(self, coeff, order):
        self.coeff = coeff
        self.order = order

    def __call__(self, x):
        return self.coeff * (x ** self.order)

    def derivative(self):
        if self.order == 1:
            return Constant(self.coeff)
        return Polynomial(self.order * self.coeff, self.order-1)


class Constant(Function):
    def __init__(self, value):
        self.value = value

    def __call__(self, x):
        return self.value

    def derivative(self):
        return Constant(0)


#####################

f = -Sine() + Constant(5.7) + Polynomial(2,3)  # f(x) = -sin(x) + 5.7 + 2*x**3
print("f(1.5)  =",f(1.5))
df = f.derivative() # f'(x) = cos(x) + 6*x**2
print("f'(1.5) =", df(1.5))

g = Sum([Sine(), Negate(Cosine()), Constant(1)]) # g(x) = sin(x) - cos(x) + 1
print("g(0.3)  =",g(0.3))
dg = g.derivative() # g'(x) = cos(x) + sin(x)
print("g'(0.3) =",dg(0.3))

h = ((-f) + g).derivative()  # h(x) = - 6*x**2 + sin(x)
print("h(3.2)  =",h(3.2))
