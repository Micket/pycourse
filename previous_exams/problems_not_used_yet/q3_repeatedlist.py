class RepeatedList:
    def __init__(self, sequence, repetitions):
        self.sequence
        self.repetitions = repetitions

    def __getitem__(self, item):
        return self.sequence[item % len(self.sequence)]

    def __len__(self):
        return self.repetitions * len(self.sequence)
        
    def __str__(self, item):
        s = '['
        for _ in range(self.repetitions):
            s += ', '.join([repr(t) for t in self.sequence])
        s += ']'
        return s
 
    def __iter__(self):
        # Would be quite a bit trickier with iterator-class. Maybe require it?
        for _ in range(self.repetitions):
            for t in self.sequence:
                yield t
