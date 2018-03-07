# Part A
class DistanceUnit:
    # Base class for all units. Empty class used to verify the unit is of the correct type.
    pass


class Meter(DistanceUnit):
    factor = 1
    abbrv = 'm'


class Foot(DistanceUnit):
    factor = 0.3048
    abbrv = 'ft'


# Part B
class Distance:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
        if not issubclass(self.unit, DistanceUnit):
            raise TypeError("Unit is not a distance unit")

# Part C
    def __add__(self, other):
        return Distance(self.value + other.value * other.unit.factor / self.unit.factor, self.unit)

    def __sub__(self, other):
        return Distance(self.value - other.value * other.unit.factor / self.unit.factor, self.unit)

    def __rmul__(self, factor):
        return Distance(self.value * factor, self.unit)

    __mul__ = __rmul__

    def __truediv__(self, other):
        if isinstance(other, Distance):
            return (self.value * self.unit.factor) / (other.value * other.unit.factor)
        else:
            return Distance(self.value / other, self.unit)

    def __str__(self):
        return str(self.value) + self.unit.abbrv



# Test it out:
meter = Distance(1, Meter)
foot = Distance(1, Foot)

x = 1.2 * meter
y = 3.7 * foot

print("x =", x)
print("y*2 =", y * 2)
print("x+y =", x + y)
print("(3.5m - 6.1ft)/5 =", (3.5 * meter - 6.1 * foot)/5)
print("x/y =", x / y)

# Output:
"""
x = 1.2m
y*2 = 7.4ft
x+y = 2.32776m
(3.5m - 6.1ft)/5 = 0.328144m
x/y = 1.0640561821664183
"""
