class FixedDecimal:
    def __init__(self, integral, fractional):
        # Strip off preceeding 0's here?
        self.integral = strip_preceeding_zeros(integral)
        # Strip off preceeding 0's here?
        self.fractional = strip_trailing_zeros(fractional)

    def __str__(self):
        return ''.join(str(d) for d in self.integral) + '.' + ''.join(str(d) for d in self.fractional)

    @staticmethod
    def from_string(numberstring):
        intstr, fracstr = numberstring.split('.')
        integral = (int(d) for d in intstr)
        fractional = (int(d) for d in fracstr)
        return FixedDecimal(integral, fractional)

    def __float__(self):
        return float(str(self))

    def __eq__(self, other):
        # Assuming additional zeros have been stripped off
        return (self.integral, self.fractional) == (other.integral, other.fractional)

    def __lt__(self, other):
        # Assuming additional zeros have been stripped off
        return (self.integral, self.fractional) > (other.integral, other.fractional)

