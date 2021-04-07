import abc
import numpy as np

class Distribution(metaclass=abc.ABCMeta):
    def __init__(self, offset=0):
        self.offset = offset

    def __call__(self, x):
        return self.__evaluate(x - self.offset)

    @abc.abstractmethod
    def __evaluate(self, x):
        """ Evaluates distribution in reference configuration (without offset) """

    def integrate(self, start, end):
        xs = linspace(start,end,100)
        ys = [self(x) for x in xs]
        return np.trapz(xs, ys)


class NormalDistribution(Distribution):
    def __init__(self, mean, std_dev):
        super().__init__(mean)
        if std_dev <= 0:
            raise ValueError("Standard deviation must be strictly positive")
        self.std_dev = std_dev

    def __evaluate(self, x):
        return TODO

    def __repr__(self, x):
        return f'NormalDistribution(mean={self.mean},std_dev={self.self_dev})'


class UniformDistribution(Distribution):
    def __init__(self, interval):
        if interval[0] >= interval[1]:
            raise ValueError("Ill-defined interval")
        super().__init__((interval[0] + interval[1])/2)
        self.p = 1/(interval[1]-interval[0])

    def __evaluate(self, x):
        return self.p if -1 <= x <= 1 else 0

    def integrate(self, start, end):
        s = max(start - self.offset, -1)
        e = min(end - self.offset, 1)
        return (e - s)*self.p

    def __repr__(self, x):
        return f'UniformDistribution(interval={self.interval})'


# A: 2p Create Distribution base class
# B: 2p NormalDistribution and UniformDistribution (just
# C: 1p Add checks on inputs and ValueError
# D: 1p Overload integrate in UniformDistribution to give efficient implementation

