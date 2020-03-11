import abc
import numpy as np

class Shape(metaclass=abc.ABCMeta):
    def __init__(self, centre):
        self.centre = centre

    def move(self, translation_vector):
        self.centre += translation_vector

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
    def __init__(self, points):
        centre = np.mean(points, axis=0)
        super().__init__(centre)
        self.points = points - centre

    def resize(self, scale: float):
        self.points *= scale

    def rotate(self, theta: float):
        m = np.array([[np.cos(theta), -np.sin(theta)],
                      [np.sin(theta), np.cos(theta)]])
        self.points = np.dot(m, self.points.T).T

    def bounding_box(self):
        return self.centre + np.min(self.points, axis=0), self.centre + np.max(self.points, axis=0)


class Rectangle(Polygon):
    def __init__(self, corner, width, height):
        super().__init__(np.array([
            corner,
            [corner[0]+width, corner[1]],
            [corner[0]+width, corner[1]+height],
            [corner[0], corner[1]+height],
        ]))


# Test cases
circle = Circle(centre=np.array([0.5, 1.0]), radius=0.5)
print(f'Circle with centre at {circle.centre} and bounding box {circle.bounding_box()}')
circle.move(np.array([-0.5, 2.0]))
circle.resize(2.0)
circle.rotate(np.pi/6)  # rotate 30 degrees
print(f'Circle with centre at {circle.centre} and bounding box {circle.bounding_box()}')

global_points = np.array([
    [0.0, 0.0],
    [3.0, 1.0],
    [2.0, 1.5],
    [1.0, 3.0],
])
poly = Polygon(global_points)
print(f'Polygon with centre at {poly.centre} and bounding box {poly.bounding_box()}')
print(f'Its first point is at {poly.points[0]} relative to its centre')
poly.move(np.array([-0.2, 0.3]))
poly.resize(2.0)
print(f'Polygon with centre at {poly.centre} and bounding box {poly.bounding_box()}')
poly.rotate(np.pi)  # rotate 180 degrees
print(f'Polygon with centre at {poly.centre} and bounding box {poly.bounding_box()}')


rec = Rectangle(corner=np.array([0., 0.]), width=6., height=4.)
print(f'Rectangle with centre at {rec.centre} and bounding box {rec.bounding_box()}')
print(f'Its first point is at {rec.points[0]} relative to its centre')
rec.move(np.array([-0.5, 0.5]))
rec.resize(0.5)
print(f'Rectangle with centre at {rec.centre} and bounding box {rec.bounding_box()}')
rec.rotate(np.pi/2)  # rotate 90 degrees
print(f'Rectangle with centre at {rec.centre} and bounding box {rec.bounding_box()}')
print(f'Its first point is at {rec.points[0]} relative to its centre')


