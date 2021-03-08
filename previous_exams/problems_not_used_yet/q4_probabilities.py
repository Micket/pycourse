import abc

class Distribution(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def probability(self, start, end):
        pass

    @abc.abstractmethod
    def __call__(self, x):
        pass


class NormalDistribution(Distribution):
    def __init__(self, mean, variance):
        self.mean = mean
        self.spread = variance

    def probability(self, start, end):
        return TODO


class UniformDistribution(Distribution):
    def __init__(self, interval):
        self.interval = interval

    def probability(self, start, end):
        return TODO


