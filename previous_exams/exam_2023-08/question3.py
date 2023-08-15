class DisjointError(ValueError):
    pass

class Interval:
    def __init__(self, low, high):
        if high < low:
            raise ValueError('"high" must be larger or equal to "low"!')
        self.low = low
        self.high = high

    def __repr__(self):
        return f'Interval({self.low}, {self.high})'

    def overlaps(self, other):
        return self.high >= other.low and other.high >= self.low

    def union(self, other):
        if self.overlaps(other):
            return Interval(min(self.low, other.low), max(self.high, other.high))
        else:
            raise DisjointError(f"{repr(self)} {repr(other)} has no overlap")

    def __neg__(self):
        return Interval(-self.high, -self.low)

    def __add__(self, other):
        return Interval(self.low + other.low, self.high + other.high)

    def __sub__(self, other):
        # Alternatively:
        # return self + (-other)
        return Interval(self.low - other.high, self.high - other.low)

    def __mul__(self, other):
        # Compute all possible extreme values low*low, low*high, high*low, high*high
        values = self.low * other.low, self.low * other.high, self.high * other.low, self.high * other.high
        return Interval(min(values), max(values))

    def __float__(self):
        return (self.high + self.low)/2

# Test code
x = Interval(1., 3.)
y = Interval(-4., 5.)
z = Interval(-10., 0.)
v = y.union(z)

print('x overlaps z =', x.overlaps(z))
print('x overlaps y =', x.overlaps(y))
print('v =', v)
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

w = x.union(Interval(4,7))  # should raise your exception
