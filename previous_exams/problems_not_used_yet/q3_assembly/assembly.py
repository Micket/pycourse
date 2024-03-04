
class MatrixAssembly:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.positions = []
        self.blocks = []

    def assemble(self, position, block):
        # TODO check size
        self.positions.append(position)
        self.blocks.append(block)

    def clear(self):
        self.positions.clear()
        self.blocks.clear()

    def size(self):
        return self.n, self.m

    def __iadd__(self, other):
        if self.size() != other.size():
            return IndexError("Matrix sizes not equal")

        m = MatrixAssembly(self.n, self.m)
        m.positions = self.positions + other.positions
        m.blocks = self.blocks + other.blocks
        return m

    def __getitem__(self, v):
        pass # TODO

    def dot(self, v):
        pass # TODO
