class Interval:
    def __init__(self, low, high):
        if high < low:
            raise ValueError("high must be larger or equal to low")
        self.low = low
        self.high = high

    def __repr__(self):
        return f'Interval({self.low}, {self.high})'

    def overlaps(self, other):
        return self.high >= other.low and other.high >= self.low

    def __neg__(self):
        return Interval(-self.high, -self.low)

    def __add__(self, x):
        return Interval(self.low + x.low, self.high + x.high)

    def __sub__(self, x):
        # Alternatively:
        # return self + (-x)
        return Interval(self.low - x.high, self.high - x.low)

    def __mul__(self, x):
        # Compute all possible extreme values low*low, low*high, high*low, high*high
        values = self.low*x.low, self.low*x.high, self.high*x.low, self.high*x.high
        return Interval(min(values), max(values))

    def __float__(self):
        return (self.high + self.low)/2


# Test code
x = Interval(1., 3.)
y = Interval(-4., 5.)
z = Interval(-10., 0.)

print('x overlaps z =', x.overlaps(z))
print('y overlaps z =', x.overlaps(y))
print('-x = ', -x)
print('-y = ', -y)
print('-z = ', -z)

print('x + y =', x+y)
print('x - y =', x-y)
print('z - x =', z-x)

print('x * y =', x*y)
print('z * y =', z*y)
print('y * y =', y*y)

print('float(x) =', float(x))
print('float(y) =', float(y))
print('float(z) =', float(z))
