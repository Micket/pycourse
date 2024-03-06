class StructuralComponent:
    @abc.abstractmethod
    def force(self, disp, vel):
        pass


class Damper(StructuralComponent):
    def __init__(self, c):
        self.c = c

    def force(self, disp, vel):
        return self.c * vel


class Spring(StructuralComponent):
    def __init__(self, k):
        self.k = k

    def force(self, disp, vel):
        return self.k * disp


class CustomSpring(StructuralComponent):
    def __init__(self, kfun):
        self.kfun

    def force(self, disp, vel):
        return self.kfun(disp)


class ParallelCoupled(StructuralComponent):
    def __init__(self, components):
        self.components = components

    def force(self, disp, vel):
        return sum([comp.force(disp, vel) for comp in self.components])


class SerieCoupled:
    def __init__(self, components):
        self.components = components

    def force(self, disp, vel):
        pass


