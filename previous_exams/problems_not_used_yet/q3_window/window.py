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

    def __len__(self):
        return len(self.array) - self.size + 1

