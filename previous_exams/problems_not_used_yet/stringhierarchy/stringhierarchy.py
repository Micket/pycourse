# Meh, this didn't turn out very good
import abc

class EncodingBase(abc.ABC):
    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def data_size(self):
        pass


class RepeatedSequences(EncodingBase):
    def __init__(self, string):
        self.sequence = [] # Todo, tricky

    def __str__(self):
        return ''.join([character*rep for char, rep in self.sequence])

    def data_size(self):
        return len(self.sequence)*(32+32)


class Uncompressed(EncodingBase):
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def data_size(self):
        return len(self.string)*32


class ConstantString(EncodingBase):
    def __init__(self, c, num):
        self.c = c
        self.num = num

    def __str__(self):
        return self.c * self.num

    def data_size(self):
        return 32 + 32

