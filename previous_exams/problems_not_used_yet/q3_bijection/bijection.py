class Bijection:
    def __init__(self, items):
        self.foward = dict()
        self.backward = dict()
        for item in items:
            self.add(item)

    def map_foward(self, item):
        self.forward[item]

    def map_backward(self, item):
        self.backward[item]

    def add(self, item):
        a, b = item

        if a in self.foward or b in self.backward:
            raise IndexError("item already mapped")

        self.foward[a] = b
        self.backward[b] = a

    def __del__(self, item):
        b = self.forward[item]
        del self.forward[item]
        del self.backward[b]

    def __iter__(self):
        return iter(self.forward)

    def __repr__(self):
        return f'Bijection({repr(forward)})'

    def __str__(self):
        return '{' + ', '.join(f'{a}::{b}' for a, b in self.forward.items()) + '}'


