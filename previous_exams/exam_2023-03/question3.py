class Bijection:
    def __init__(self, items=()):
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

    def delete(self, first=None, second=None):
        if first is not None and second is not None:
            raise ValueError(f"Only specify one item for delete")
        elif first is None and second is None:
            raise ValueError(f"Must specify one item for delete")

        if first is not None and first in self.forward:
            second = self.forward[first]
            del self.forward[first]
            del self.backward[second]
        elif second is not None and second in self.backward:
            first = self.backward[second]
            del self.backward[second]
            del self.forward[first]
        else:
            raise IndexError(f"can't delete non-mapped item first={first}, second={second}")

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
db.delete(second=3)
print(db)
db.delete(first='a')
print(db)
# db.delete(first='x')  # should raise an exception
