class DistanceUnit:
    # Base class for all units. Empty class used to verify the unit is of the correct type.
    pass


class Meter(DistanceUnit):
    factor = 1
    abbrv = 'm'


class Foot(DistanceUnit):
    factor = 0.3048
    abbrv = 'ft'


class Distance:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
        if not issubclass(self.unit, DistanceUnit):
            raise TypeError("Unit is not a distance unit")

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

x = 3 * meter
y = 2.3 * foot

print("x =", x)
print("y*2 =", y * 2)
print("x+y =", x + y)
print("(2.5m - 4ft)/5 =", (2.5 * meter - 4 * foot)/5)
print("x/y =", x / y)

# Output:
"""
x = 3m
y*2 = 4.6ft
x+y = 3.70104m
(2.5m - 4ft)/5 = 0.25616m
x/y = 4.279356384799726
"""