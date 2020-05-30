import abc

class Crypto(abc.ABC):
    @abc.abstractmethod
    def encode(self, s: str):
        pass

    @abc.abstractmethod
    def decode(self, s: str):
        pass


class PirateLanguage(Crypto):
    def encode(self, s):
        return s.replace('b', 'bob').replace('B', 'Bob')

    def decode(self, s):
        return s.replace('Bob', 'B').replace('bob', 'b')


class CharacterCrypto(Crypto):
    @abc.abstractmethod
    def encode_chat(self, c):
        """ Encodes a single character """

    @abc.abstractmethod
    def decode_chat(self, c):
        """ Encodes a single character """

    def encode(self, s: str):
        return ''.join([self.encode_char(c) for c in s])

    def decode(self, s: str):
        return ''.join([self.decode_char(c) for c in s])


class Rotator(CharacterCrypto):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, offset):
        self.offset = offset

    @staticmethod
    def shift(c, offset):
        new_c = self.alphabet[(self.alphabet.find(c.lower()) + offset % len(alphabet))]
        return new_c if c.islower() else new_c.upper()

    def encode_char(self, c):
        return shift(c, self.offset)

    def decode_char(self, c):
        return shift(c, -self.offset)


class Replacer(CharacterCrypto):
    def __init__(self, cdict):
        self.cdict = cdict 
        self.rdict = {v:k for k, v in cdict.items()}

    def encode_char(self, c):
        new_c = cdict[c.lower()]
        return new_c if c.islower() else new_c.upper()

    def decode_char(self, c):
        new_c = cdict[c.lower()]
        return new_c if c.islower() else new_c.upper()



