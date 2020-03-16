---
header-includes:
        - \usepackage[left=1.9cm, right=1.9cm, top=1.5cm, bottom=1.9cm]{geometry}
---

# Question 4: Class hierarchy for shapes (8p)

As part of creating an application for making presentations, you are given the task of implementing support for adding simple 2D-shapes that can be moved and rotated.

For convenience, you can use NumPy arrays to perform the transformations inside the different shape types.

Part A (2p)
-----------
**Task:** Write a base class `Shape` that stores the `centre` position of the shape. It should have:

- The method `.move(translation_vector)` that moves the whole shape by the given the vector.
- The abstract method `.resize(scale)` that scales the whole shape around the centre point.
- The abstract method `.rotate(theta)` that rotates the whole shape $\theta$ radians around the centre point.
- The abstract method `.bounding_box()` that computes and returns the lower left and upper right coordinates of the rectangle/box that covers the shape.

**Hint:** Rotation of a vector $v$ can be done with a rotation matrix $R$: $v' = R(\theta) \cdot v$ where
$R(\theta) = \begin{pmatrix} \cos(\theta) & -\sin(\theta) \\ \sin(\theta) & \cos(\theta) \end{pmatrix}$

![Example shape being rotated](rotate_polygon.png)

Part B (2p)
-----------
**Task:** Write the subclass `Circle` which represents a perfect circle. Its constructor should take the centre point coordinate, and a radius.

**Example:**
```python
circle = Circle(centre=np.array([0.5, 1.0]), radius=0.5)
print(f'Circle with centre at {circle.centre} and bounding box {circle.bounding_box()}')
circle.move(np.array([-0.5, 2.0]))
circle.resize(2.0)
circle.rotate(np.pi/6)  # rotate 30 degrees
print(f'Circle with centre at {circle.centre} and bounding box {circle.bounding_box()}')
```

**Output:**
```
Circle with centre at [0.5 1. ] and bounding box (array([0. , 0.5]), array([1. , 1.5]))
Circle with centre at [0. 3.] and bounding box (array([-1.,  2.]), array([1., 4.]))
```

\newpage
Part C (3p)
-----------
**Task:** Write the subclass `Polygon` which represents the lines looped through a set of points.
Its constructor should take a NumPy array of points, but store its values relative to the centre (defined by the average of all points).

**Example:**
```python
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
```

**Output:**
```
Polygon with centre at [1.5   1.375] and bounding box (array([0., 0.]), array([3., 3.]))
Its first point is at [-1.5   -1.375] relative to its centre
Polygon with centre at [1.3   1.675] and bounding box (array([-1.7  , -1.075]), array([4.3  , 4.925]))
Polygon with centre at [1.3   1.675] and bounding box (array([-1.7  , -1.575]), array([4.3  , 4.425]))
```

Part D (1p)
-----------
**Task:** For added convenience, introduce a subclass of `Polygon` named `Rectangle`.
Its constructor should take the lower left corner as a NumPy vector, and the width and height, and creates a rectangular set of points.

**Example:**
```python
rec = Rectangle(corner=np.array([0., 0.]), width=6., height=4.)
print(f'Rectangle with centre at {rec.centre} and bounding box {rec.bounding_box()}')
print(f'Its first point is at {rec.points[0]} relative to its centre')
rec.move(np.array([-0.5, 0.5]))
rec.resize(0.5)
print(f'Rectangle with centre at {rec.centre} and bounding box {rec.bounding_box()}')
rec.rotate(np.pi/2)  # rotate 90 degrees
print(f'Rectangle with centre at {rec.centre} and bounding box {rec.bounding_box()}')
print(f'Its first point is at {rec.points[0]} relative to its centre')
```

**Output:**
```
Rectangle with centre at [3. 2.] and bounding box (array([0., 0.]), array([6., 4.]))
Its first point is at [-3. -2.] relative to its centre
Rectangle with centre at [2.5 2.5] and bounding box (array([1. , 1.5]), array([4. , 3.5]))
Rectangle with centre at [2.5 2.5] and bounding box (array([1.5, 1. ]), array([3.5, 4. ]))
Its first point is at [ 1.  -1.5] relative to its centre
```


