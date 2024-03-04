class Decimal:
    def __init__(self, digits, exponent):
        self.digits = digits
        self.exponent = exponent
        while self.digits != 0 and self.digits % 10 == 0:
            self.digits = self.digits // 10
            self.exponent += 1

    @staticmethod
    def from_string(numberstring):
        if '.' in numberstring:
            whole, decimals = numberstring.split('.')
            exponent = -len(decimals)
            digits = int(numberstring.replace('.', ''))
            return Decimal(digits, exponent)
        else:
            return Decimal(int(numberstring), 0)

    def __str__(self):
        if self.exponent >= 0:
            return str(self.digits) + '0'*self.exponent
        else:
            x = str(self.digits)
            a = x[:self.exponent]
            b = x[self.exponent:]
            return f'{a}.{b}'

    def __float__(self):
        return float(self.digits * 10**self.exponent)

    def __eq__(self, other):
        return (self.exponent, self.digits) == (other.exponent, other.digits)

    def __mul__(self, other):
        return Decimal(self.digits*other.digits, self.exponent + other.exponent)

    def __add__(self, other):
        if self.exponent < other.exponent:
            ediff = other.exponent - self.exponent
            return Decimal(self.digits + other.digits*10**ediff, self.exponent)
        elif self.exponent > other.exponent:
            return other + self
        else:
            return Decimal(self.digits + other.digits, self.exponent)

    #def __lt__(self, other):
    #    return (self.exponent, self.digits) < (other.exponent, other.digits)  # TODO sign

a = Decimal(3141592653589793238462643383279502884197, -39)
b = Decimal.from_string('41.00000000000000000000000000000000000000000000000000000000000000001')
c = Decimal.from_string('900000000000000000000000000000000000000000001')
d = Decimal.from_string('10000000000000000000000000000000000000000000')
#print(a)
#print(b)
#print(c)
#print(float(c))
#print(a*a)

#print(a.exponent)
#print(a+a)
#print(b+b)
print(a+b)
print(c+b)
print(c+d)

# 1.1 + 1.02   =   11*10^-1  +  102*10^-2   =  110*10^-1   +  102*10^-2 == (110 + 102) * 10^-2
