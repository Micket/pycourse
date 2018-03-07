import abc

class MeshSelection(metaclass=abc.ABCMeta):
    def __init__(self, triangles, coords):
        self.triangles = triangles
        self.coords = coords

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def node_list(self):
        pass

    def bounding_box(self):
        nodes = self.node_list()
        return amin(self.coords[nodes], axis=0), amax(self.coords[nodes], axis=0)


class NodeSelection(MeshSelection):
    def __init__(self, triangles, coords):
        super().__init__(triangles, coords)
        self.selected_nodes = []

    def add_node(self, node):
        self.selected_nodes.append(node)

    def area(self):
        return 0

    def node_list(self):
        return self.selected_nodes


class AreaSelection(MeshSelection):
    def __init__(self, triangles, coords):
        super().__init__(triangles, coords)
        self.selected_triangles = []

    def add_triangle(self, triangle):
        self.selected_triangles.append(triangle)

    @staticmethod
    def triangle_area(cs):
        x0, x1, x2 = cs[:,0]
        y0, y1, y2 = cs[:,1]
        return 0.5 * abs(x0*(y1-y2) + x1*(y2-y0) + x2*(y0-y1))

    def area(self):
        a = 0
        for i in self.selected_triangles:
            a += self.triangle_area(coords[self.triangles[i]])
        return a

    def node_list(self):
        n = set()
        for i in self.selected_triangles:
            n.update(self.triangles[i])
        return list(n)


class EdgeSelection(MeshSelection):
    edge_nodes = [[0,1],[1,2],[2,0]]

    def __init__(self, triangles, coords):
        super().__init__(triangles, coords)
        self.selected_edges = []

    def add_edge(self, triangle, edge):
        self.selected_edges.append((triangle,edge))

    def area(self):
        return 0

    def node_list(self):
        n = set()
        for t, e in self.selected_edges:
            n.update(self.triangles[t][self.edge_nodes[e]])
        return list(n)


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
