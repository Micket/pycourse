class EachColumn:
    # Loops over each column in a np matrix
    # TODO: verify that there isn't just a finished one in np already, that could make this question to trivial

    def EachColumnIt:
        def __init_(self, matrix):
            self.matrix = matrix
            self.i = 0

        def __next__(self):
            if self.i == matrix.shape[1]
                raise StopIteration
            else:
                col = self.matrix[:,i]
                self.i += 1
                return col

    def __init__(self, matrix):
        self.matrix = matrix

    def __getitem__(self, item):
        return self.matrix[:,item]

    def __setitem__(self, item, values):
        self.matrix[:,item] = values

    def __len__(self):
        return self.matrix.shape[1]

    def __iter__(self):
        return EachColumnIt(self.matrix)

# Alternative (just iterator part)
def each_column(matrix):
    for i in range(matrix.shape[1]):
        yield matrix[:,i]



