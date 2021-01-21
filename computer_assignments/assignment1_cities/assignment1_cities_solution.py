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


def plot_points(coord_list, indices, path, savefig=True):
    x = coord_list[:, 0]
    y = coord_list[:, 1]
    fig, ax = plt.subplots()
    plt.title("Shortest path")

    ax.scatter(x, y, marker='.', color='red', zorder=0)

    lines = LineCollection(coord_list[indices, :], zorder=1, colors=(0.5, 0.5, 0.5), linewidths=0.5, alpha=0.75)
    ax.add_collection(lines)

    path_line = LineCollection([coord_list[path, :]], zorder=2)
    ax.add_collection(path_line)
    ax.axis('equal')
    if savefig:
        plt.savefig("final_path.pdf")
    plt.show()


def construct_graph_connections(coord_list, radius):
    indices = []
    distances = []
    for i, i_coord in enumerate(coord_list):
        for j in range(i+1, len(coord_list)):
            j_coord = coord_list[j]
            d = np.linalg.norm(i_coord - j_coord)
            if d <= radius:
                distances.append(d)
                indices.append((i, j))
    return np.array(indices), np.array(distances)


def construct_fast_graph_connections(coord_list, radius):
    tree = cKDTree(coord_list)
    indices = []
    distances = []
    for i, i_coord in enumerate(coord_list):
        for j in tree.query_ball_point(i_coord, radius):
            if j > i:
                j_coord = coord_list[j]
                d = np.linalg.norm(i_coord - j_coord)
                distances.append(d)
                indices.append((i, j))
    return np.array(indices), np.array(distances)


def construct_graph(indices, distances, N):
    return sp.csr_matrix((distances, indices.transpose()), shape=(N, N))


def compute_path(predecessor_matrix, start_node, end_node):
    position = end_node
    path = [end_node]
    while position != start_node:
        position = predecessor_matrix[position]
        path.append(position)
    path.reverse()
    return path


#input_file, radius, start_city, end_city = 'SampleCoordinates.txt', 0.08, 0, 5
input_file, radius, start_city, end_city = 'HungaryCities.txt', 0.005, 311, 702
#input_file, radius, start_city, end_city = 'GermanyCities.txt', 0.0025, 1573, 10584

coordinates = read_coordinate_file(input_file)
#indices, distances = construct_graph_connections(coordinates, radius)
indices, distances = construct_fast_graph_connections(coordinates, radius)

graph = construct_graph(indices, distances, len(coordinates))
path_distances, predecessors = sp.csgraph.shortest_path(graph, indices=start_city, method='D', directed=False, return_predecessors=True)
shortest_path = compute_path(predecessors, start_city, end_city)

shortest_path_cost = path_distances[end_city]

print("Shortest path from {} to {} is: {}".format(start_city, end_city, shortest_path))
print("Total distance: {}".format(shortest_path_cost))

plot_points(coordinates, indices, shortest_path)

