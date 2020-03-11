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

