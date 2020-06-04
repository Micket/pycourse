import abc

class Crypto(abc.ABC):
    @abc.abstractmethod
    def encode(self, s: str) -> str:
        pass

    @abc.abstractmethod
    def decode(self, s: str) -> str:
        pass


class PirateLanguage(Crypto):
    consonants = 'bcdfghjklmnpqrstvwx'

    def encode(self, s: str) -> str:
        for c in self.consonants:
            s = s.replace(c, c + 'o' + c).replace(c.upper(), c.upper() + 'o' + c)
        return s

    def decode(self, s: str) -> str:
        for c in self.consonants:
            s = s.replace(c + 'o' + c, c).replace(c.upper() + 'o' + c, c.upper())
        return s


class CharacterCrypto(Crypto):
    @abc.abstractmethod
    def encode_char(self, c):
        """ Encodes a single character """

    @abc.abstractmethod
    def decode_char(self, c):
        """ Decodes a single character """

    def encode(self, s: str):
        return ''.join([self.encode_char(c) for c in s])

    def decode(self, s: str):
        return ''.join([self.decode_char(c) for c in s])


class Rotator(CharacterCrypto):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, offset: int):
        self.offset = offset

    @staticmethod
    def shift(c, offset: int):
        p = Rotator.alphabet.find(c.lower())
        if p == -1:
            return c
        else:
            new_c = Rotator.alphabet[(p + offset) % len(Rotator.alphabet)]
            return new_c if c.islower() else new_c.upper()

    def encode_char(self, c):
        return self.shift(c, self.offset)

    def decode_char(self, c):
        return self.shift(c, -self.offset)


class Replacer(CharacterCrypto):
    def __init__(self, cdict: dict):
        self.cdict = cdict 
        self.rdict = {v:k for k, v in cdict.items()}

    def encode_char(self, c):
        if c.lower() not in self.cdict:
            return c
        else:
            new_c = self.cdict[c.lower()]
            return new_c if c.islower() else new_c.upper()

    def decode_char(self, c):
        if c.lower() not in self.rdict:
            return c
        else:
            new_c = self.rdict[c.lower()]
            return new_c if c.islower() else new_c.upper()

# Tests
message = 'Robber Bob robs ten banks'
print('Original message:',  message)

# Part B
pcrypto = PirateLanguage()
psecret = pcrypto.encode(message)
print('Pirate encrypted:', psecret)
assert pcrypto.decode(psecret) == message # Decoding should give us back the original message

# Part C
# Check shift helper works correctly
assert Rotator.shift('a', 1) == 'b' # a+1 should become b
assert Rotator.shift('a', -1) == 'z' # a-1 should become z
assert Rotator.shift('g', 13) == 't' # g+13 should become t
assert Rotator.shift(' ', 13) == ' ' # characters not present in the english alphabet are not replaced.

rotcrypto = Rotator(13)
rotsecret = rotcrypto.encode(message)
print('Rotate encrypted:', rotsecret)
assert rotcrypto.decode(rotsecret) == message # Decoding should give us back the original message

# Part D
repcrypto = Replacer({x:y for x,y in zip('abcdefghijklmnopqrstuvwxyz', 'kfghiwxucdyzlmveqabpnojrst')})
repsecret = repcrypto.encode(message)
print('Replace encrypted:', repsecret)
assert repcrypto.decode(repsecret) == message # Decoding should give us back the original message

