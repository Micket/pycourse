import abc
import numpy as np

class Shape(metaclass=abc.ABCMeta):
    def __init__(self, centre):
        self.centre = centre

    def move(self, distance):
        self.centre -= distance

    @abc.abstractmethod
    def resize(self, scale: float):
        """ Scale around centre point """

    @abc.abstractmethod
    def rotate(self, theta: float):
        """ Rotate around centre point """

    @abc.abstractmethod
    def bounding_box(self):
        """ Rotate box (in global coordinates) """


class Circle(Shape):
    def __init__(self, centre, radius: float):
        super().__init__(centre)
        self.radius = radius

    def resize(self, scale: float):
        self.radius *= scale

    def rotate(self, theta: float):
        pass

    def bounding_box(self):
        return self.centre - self.radius, self.centre + self.radius


class Polygon(Shape):
    def __init__(self, nodes):
        centre = np.mean(nodes, axis=0)
        super().__init__(centre)
        self.nodes = nodes - centre
        print(nodes, self.nodes)

    def resize(self, scale: float):
        self.nodes *= scale

    def rotate(self, theta: float):
        m = np.array([[np.cos(theta), -np.sin(theta)],
                      [np.sin(theta), np.cos(theta)]])
        self.nodes = np.dot(m, self.nodes.T).T

    def bounding_box(self):
        return self.centre + np.min(self.nodes, axis=0), self.centre + np.max(self.nodes, axis=0)

# Test cases
coords = np.array([
    [0.0, 0.0],
    [3.0, 1.0],
    [2.0, 1.5],
    [1.0, 3.0],
])
poly = Polygon(coords)
print('Polygon with centre at {} and bounding box {}'.format(poly.centre, poly.bounding_box()))
print('Its first coordinate is at {} relative to its centre'.format(poly.coords[0]))
poly.move(np.array([-0.2, 0.3]))
poly.resize(2.0)
print('Polygon with centre at {} and bounding box {}'.format(poly.centre, poly.bounding_box()))
poly.rotate(np.pi/6) # rotate 30 degrees
print('Polygon with centre at {} and bounding box {}'.format(poly.centre, poly.bounding_box()))

circle = Circle(np.array([0.5, 1.0]), 0.5)
print('Circle with centre at {} and bounding box {}'.format(circle.centre, circle.bounding_box()))
circle.move(np.array([-0.5, 2.0]))
circle.resize(2.0)
circle.rotate(np.pi/6) # rotate 30 degrees
print('Circle with centre at {} and bounding box {}'.format(circle.centre, circle.bounding_box()))


