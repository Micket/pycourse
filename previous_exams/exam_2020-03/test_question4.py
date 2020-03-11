circle = Circle(np.array([0.5, 1.0]), 0.5)
print('Circle with centre at {} and bounding box {}'.format(circle.centre, circle.bounding_box()))
circle.move(np.array([-0.5, 2.0]))
circle.resize(2.0)
circle.rotate(np.pi/6)  # rotate 30 degrees
print('Circle with centre at {} and bounding box {}'.format(circle.centre, circle.bounding_box()))

global_nodes = np.array([
    [0.0, 0.0],
    [3.0, 1.0],
    [2.0, 1.5],
    [1.0, 3.0],
])
poly = Polygon(global_nodes)
print('Polygon with centre at {} and bounding box {}'.format(poly.centre, poly.bounding_box()))
print('Its first coordinate is at {} relative to its centre'.format(poly.nodes[0]))
poly.move(np.array([-0.2, 0.3]))
poly.resize(2.0)
print('Polygon with centre at {} and bounding box {}'.format(poly.centre, poly.bounding_box()))
poly.rotate(np.pi)  # rotate 180 degrees
print('Polygon with centre at {} and bounding box {}'.format(poly.centre, poly.bounding_box()))


rec = Rectangle(np.array([0., 0.]), 6., 4.)
print('Rectangle with centre at {} and bounding box {}'.format(rec.centre, rec.bounding_box()))
print('Its first coordinate is at {} relative to its centre'.format(rec.nodes[0]))
rec.move(np.array([-0.5, 0.5]))
rec.resize(0.5)
print('Rectangle with centre at {} and bounding box {}'.format(rec.centre, rec.bounding_box()))
rec.rotate(np.pi/2)  # rotate 90 degrees
print('Rectangle with centre at {} and bounding box {}'.format(rec.centre, rec.bounding_box()))
print('Its first coordinate is at {} relative to its centre'.format(rec.nodes[0]))

