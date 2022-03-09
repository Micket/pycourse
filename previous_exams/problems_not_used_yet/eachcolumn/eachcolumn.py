class EachColumn:
    def __init__(self, matrix):
        self.matrix = matrix

    def __getitem__(self, item):
        return self.matrix[:,item]

    def __len__(self):
        return self.matrix.shape[1]

    def __iter__(self):
        class EachColumnIt:
            def __init__(self, matrix):
                self.i = 0
                self.cols = cols

            def __next__(self):
                if i >= len(self.cols):
                    raise StopIteration
                col = cols[i]
                i += 1
                return col

        return EachColumnIt(self)

