class DeInterleave:
    def __init__(self, data):
        self.data = data
        if len(data) % 2 != 0:
            raise Error

    def __iter__(self):
        class DeInterleavIterator:
            def __init__(self, it):
                self.it = it

            def __next__(self):
                return next(self.it), next(self.it)

        return DeInterleavIterator(iter(self.data))


data = [0, 14, 54, 20, 35, 22, 31, 76]

for x, y in DeInterleave(data):
    print('x = ', x, 'and y = ', y)

