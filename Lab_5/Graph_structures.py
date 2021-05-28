class Edge:
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight


class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    # to make the class work with a min-heap
    def __lt__(self, other):
        return self.weight < other.weight


class Graph:
    def __init__(self, edges, N):
        # adjacency list
        self.adj = [[] for _ in range(N)]

        # adding edges to the graph
        for edge in edges:
            self.adj[edge.source].append(edge)
