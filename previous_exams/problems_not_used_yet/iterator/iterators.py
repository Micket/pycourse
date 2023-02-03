class Window:
    # A sliding window loops over multiple subsequent values per iteration.
    # Window([1,2,3,4,5], 2)  -> [1,2], [2, 3], [3, 4], [4, 5]

    class WindowIt:
        def __init__(self, window):
            self.window = window
            self.it = iter(window.array)
            self.prev_values = (None,) + (next(self.it) for _ in range(self.window.size)-1)

        def __next__(self, window):
            self.values = self.values[:1]
            self.values.append(next(self.it))
            return self.values

    def __iter__(self):
        return WindowIt(self)

    def __init__(self, array, size=2):
        self.array = array
        self.size = size



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

    def __iter__(self):
        return WindowIt(self.matrix)

    def __init__(self, matrix):
        self.matrix = matrix


# Alternative
def each_column(matrix):
    for i in range(matrix.shape[1]):
        yield matrix[:,i]



