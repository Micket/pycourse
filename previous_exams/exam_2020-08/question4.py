import abc

class GeneratorVector(abc.ABC):
    def __init__(self, length: int):
        self.length = length

    def __len__(self):
        return self.length

    def collect(self) -> list:
        """Collects generated valued into normal list."""
        return [self[i] for i in range(self.length)]

    @abc.abstractmethod
    def __getitem__(self, i: int):
        pass

    # Optional: Also support c + v
    def __radd__(self, c: float):
        return self + c

    # Optional: Also support c * v
    def __rmul__(self, c: float):
        return self * c


class ConstantVector(GeneratorVector):
    def __init__(self, constant, length: int):
        super().__init__(length)
        self.constant = constant

    def __getitem__(self, i: int):
        return self.constant

    def __add__(self, c: float):
        return ConstantVector(self.constant + c, self.length)

    def __mul__(self, c: float):
        return ConstantVector(self.constant * c, self.length)

    def __repr__(self) -> str:
        return f"ConstantVector({self.constant}, {self.length})"


class LinspaceVector(GeneratorVector):
    def __init__(self, start: float, end: float, length: int):
        super().__init__(length)
        self.start = start
        self.end = end
        self.delta = end - start

    def __getitem__(self, i: int):
        return self.start + (self.delta * i) / float(self.length - 1)

    def __add__(self, c: float):
        return LinspaceVector(self.start + c, self.end + c, self.length)

    def __mul__(self, c: float):
        return LinspaceVector(self.start * c, self.end * c, self.length)

    def __repr__(self) -> str:
        return f"LinspaceVector({self.start}, {self.end}, {self.length})"


class FunctionVector(GeneratorVector):
    def __init__(self, f, length: int):
        super().__init__(length)
        self.f = f

    def __getitem__(self, i: int):
        return self.f(i)

    def __add__(self, c: float):
        return FunctionVector(lambda i: self.f(i)+c, self.length)

    def __mul__(self, c: float):
        return FunctionVector(lambda i: self.f(i)*c, self.length)

    def __repr__(self) -> str:
        return f"FunctionVector({self.f}, {self.length})"

# Test code:
def test_vector(v):
    print("Vector:", v)
    print("Length:", len(v))
    print("At pos 1 and 3:", v[1], v[3])
    print("Collected:", v.collect())

    print("Adding 3")
    v2 = v + 3
    print("Vector:", v2)
    print("Length:", len(v2))
    print("At pos 1 and 3:", v2[1], v2[3])
    print("Collected:", v2.collect())

    print("and mutliplying by 0.5")
    v3 = v2 * 0.5
    print("Vector:", v3)
    print("Length:", len(v3))
    print("At pos 1 and 3:", v3[1], v3[3])
    print("Collected:", v3.collect())
    print("")

cv = ConstantVector(3.5, 5)
test_vector(cv)

lv = LinspaceVector(0.5, 1.5, 5)
test_vector(lv)

from math import sqrt
fv = FunctionVector(sqrt, 5)
test_vector(fv)

