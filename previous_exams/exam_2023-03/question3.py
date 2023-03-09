class Bijection:
    def __init__(self, items = ()):
        self.forward = dict()
        self.backward = dict()
        for item in items:
            self.add(item)

    def map_forward(self, item):
        return self.forward[item]

    def map_backward(self, item):
        return self.backward[item]

    def add(self, item):
        a, b = item

        if a in self.forward or b in self.backward:
            raise ValueError("item already mapped")

        self.forward[a] = b
        self.backward[b] = a

    def delete(self, i):
        if i in self.forward:
            j = self.forward[i]
            del self.forward[i]
            del self.backward[j]
        elif i in self.backward:
            j = self.backward[i]
            del self.backward[i]
            del self.forward[j]
        else:
            raise IndexError(f"can't delete non-mapped item {i}")

    def __iter__(self):
        return iter(self.forward.items())

    def __repr__(self):
        return f'Bijection({repr(forward)})'

    def __str__(self):
        return '{' + ', '.join(f'{a}::{b}' for a, b in self) + '}'


# Test
db = Bijection()
db2 = Bijection((('a', 1), ('b', 2)))

db.add(('a', 1))
db.add(('b', 2))
db.add(('c', 3))

assert db.map_forward('b') == 2
assert db.map_backward(1) == 'a'

for a, b in db2:
    print(a, '<-->', b)

print()
print(db)
db.delete(3)
print(db)
