import AdjacencyGraph
import bfs

# this python program is able to use functions that read in data input from a
# .txt file containing latitudes and longitudes of various parts of the city of
# Edmonton


def least_cost_path(graph, start, dest, cost):
"""Find and return a least cost path in graph from start vertex to dest vertex.
    Efficiency: If E is the number of edges, the run-time is
      O( E log(E) ).
    Args:
      graph (Graph): The digraph defining the edges between the
        vertices.
      start: The vertex where the path starts. It is assumed
        that start is a vertex of graph.
      dest:  The vertex where the path ends. It is assumed
        that start is a vertex of graph.
      cost:  A function, taking the two vertices of an edge as
        parameters and returning the cost of the edge. For its
        interface, see the definition of cost_distance.
    Returns:
      list: A potentially empty list (if no path can be found) of
        the vertices in the graph. If there was a path, the first
        vertex is always start, the last is always dest in the list.
        Any two consecutive vertices correspond to some
        edge in graph.
"""


def cost_distance(u, v):
'''Computes and returns the straight-line distance between the two vertices u and v.
    Args:
        u, v: The ids for two vertices that are the start and
          end of a valid edge in the graph.
        Returns:
          numeric value: the distance between the two vertices.
'''

''' This funtion below needs to be modified in order to read the Edmonton
    information properly and convert latitude values into 100000ths'''


def read_city_graph(filename):
    # create graph g with UndirectedAdjacencyGraph class
    g = UndirectedAdjacencyGraph()

    # open the Edmonton Grph .csv file
    Edmonton_Graph = open(filename)
    Graph_Reader = csv.reader(Edmonton_Graph)  # read entire .csv file
    # read each line to determine whether to add vertices or add edges
    for i in Graph_Reader:
        # split by commas
        if i[0] == 'V':  # when the line is describing a vertex
            g.add_vertex(i[1])
        elif i[0] == 'E':  # when the line is describing an edge
            g.add_edge((i[1], i[2]))

    return g
