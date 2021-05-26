class RepeatedList:
    def __init__(self, sequence, repetitions):
        self.sequence = sequence
        self.repetitions = repetitions

    def __getitem__(self, item):
        return self.sequence[item % len(self.sequence)]

    def __len__(self):
        return self.repetitions * len(self.sequence)
        
    def __str__(self):
        if len(self.sequence) == 0: return '[]'
        s = ', '.join([repr(t) for t in self.sequence])
        return '[' + ', '.join([s for _ in range(self.repetitions)]) + ']'
 
    def expand(self):
        return self.sequence * self.repetitions

    def __iter__(self):
        # Would be quite a bit trickier with iterator-class. Maybe require it?
        #for _ in range(self.repetitions):
        #    for t in self.sequence:
        #        yield t
        return RepeatedListIterator(self)


class RepeatedListIterator:
    def __init__(self, repeatedlist):
        self.repeatedlist = repeatedlist
        self.repetition = 0
        self.seqiter = iter(self.repeatedlist.sequence)

    def __next__(self):
        if self.repetition < self.repeatedlist.repetitions:
            try:
                return next(self.seqiter)
            except StopIteration:
                self.repetition += 1
                if self.repetition == self.repeatedlist.repetitions:
                    raise
                self.seqiter = iter(self.repeatedlist.sequence)
                return next(self.seqiter)
        else:
            raise StopIteration


x = RepeatedList([1,2,3], 3)
print(x)
for i, v in enumerate(x):
    print(f'{i}: {v}')
assert len(y) == 9
assert len(y.expand()) == 9
print(y.expand())

y = RepeatedList([1,2,3], 1)
print(y)
assert len(y) == 0
for i, v in enumerate(y):
    assert False  # Should not occur

z = RepeatedList([], 3)
print(z)
assert len(y) == 0
for i, v in enumerate(z):
    assert False  # Should not occur

