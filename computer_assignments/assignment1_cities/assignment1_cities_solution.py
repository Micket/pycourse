from math import log, tan, pi
import numpy as np
import scipy.sparse as sp
from scipy.spatial import cKDTree
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


def mercator_projection(R, latitude, longitude):
    x = R * pi * longitude / 180
    y = R * log(tan(pi*(1/4+latitude/360)))
    return x, y


def read_coordinate_file(filename):
    coordinates = []
    with open(filename) as file:
        for line in file:
            a, b = line.strip(' \n{}').split(',')
            coordinate = mercator_projection(1.0, float(a), float(b))
            coordinates.append(coordinate)
    return np.array(coordinates)


def plot_points(coord_list, indices, path):
    x = coord_list[:, 0]
    y = coord_list[:, 1]
    plt.scatter(x, y, marker='.', color='red', zorder=1)

    ax = plt.gca()
    lines = LineCollection(coord_list[indices, :], zorder=0, colors=(0.5, 0.5, 0.5), linewidths=0.5)
    ax.add_collection(lines)

    path_line = LineCollection([coord_list[path, :]], zorder=2)
    ax.add_collection(path_line)
    
    ax.axis('equal')
    plt.show()


def construct_graph_connections(coord_list, radius):
    indices = []
    costs = []
    for i, i_coord in enumerate(coord_list):
        for j in range(i+1, len(coord_list)):
            j_coord = coord_list[j]
            d = np.linalg.norm(i_coord - j_coord)
            if d <= radius:
                costs.append(pow(d, 9/10))
                indices.append((i, j))
    return np.array(indices), np.array(costs)


def construct_fast_graph_connections(coord_list, radius):
    tree = cKDTree(coord_list)
    indices = []
    costs = []
    for i, i_coord in enumerate(coord_list):
        for j in tree.query_ball_point(i_coord, radius):
            if j > i:
                j_coord = coord_list[j]
                d = np.linalg.norm(i_coord - j_coord)
                costs.append(pow(d, 9/10))
                indices.append((i, j))
    return np.array(indices), np.array(costs)


def construct_graph(indices, costs, N):
    return sp.csr_matrix((costs, indices.transpose()), shape=(N, N))


def compute_path(predecessor_matrix, start_node, end_node):
    position = end_node
    path = [end_node]
    while position != start_node:
        position = predecessor_matrix[position]
        path.append(position)
    return path


#input_file, radius, start_city, end_city = 'SampleCoordinates.txt', 0.08, 0, 5
#input_file, radius, start_city, end_city = 'HungaryCities.txt', 0.005, 311, 702
input_file, radius, start_city, end_city = 'GermanyCities.txt', 0.0025, 1573, 10584

coordinates = read_coordinate_file(input_file)
#indices, costs = construct_graph_connections(coordinates, radius)
indices, costs = construct_fast_graph_connections(coordinates, radius)

print(costs)
print(indices)

graph = construct_graph(indices, costs, len(coordinates))
path_costs, predecessors = sp.csgraph.shortest_path(graph, indices=start_city, method='D', directed=False, return_predecessors=True)
cheapest_path = compute_path(predecessors, start_city, end_city)

cheapest_path_cost = path_costs[end_city]

plot_points(coordinates, indices, cheapest_path)

