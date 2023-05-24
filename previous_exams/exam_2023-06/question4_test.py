# Testing it out
from numpy import loadtxt, int32, amin, amax
coords = loadtxt('coords.txt')
triangles = loadtxt('triangles.txt', dtype=int32)

nsel = NodeSelection(triangles, coords)
nsel.add_node(3)
nsel.add_node(4)
print('nsel:', nsel.node_list())
print('nsel:', nsel.bounding_box())
print('nsel:', nsel.area())

asel = AreaSelection(triangles, coords)
asel.add_triangle(3)
asel.add_triangle(4)
print('asel:', asel.node_list())
print('asel:', asel.bounding_box())
print('asel:', asel.area())

esel = EdgeSelection(triangles, coords)
esel.add_edge(3, 1)
esel.add_edge(4, 0)
print('esel:', esel.node_list())
print('esel:', esel.bounding_box())
print('esel:', esel.area())
