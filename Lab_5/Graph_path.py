import sys
from heapq import heappop, heappush
import argparse
from typing import Counter

# creating a matrix from a list of values
def create_matrix(val_list, n):
    matrix = [[0 for x in range(n)]for y in range(n)]
    i = 0
    for y in range(n):
        for x in range(n):
            matrix[y][x] = val_list[i]
            i = i+1
    return matrix


# creating a list of numbers from a grid given in the file, returns also places with 0's
def get_val_list(path):
    val_list = []
    zero_list = []
    count = 0
    with open(path, 'r') as fp:
        values = fp.read()
        for line in values:
            for number in line:
                if (number == '\n'):
                    continue
                val_list.append(int(number))
                if int(number) == 0:
                    zero_list.append(count)
                count = count+1
    return val_list, zero_list


# creating a list of edges from a grid (matrix)
def create_edges_list(matrix, N):
    edges = []
    for y in range(N):
        for x in range(N):
            if y < (N-1):
                edges.append(Edge(N*y+x, N*(y+1)+x, matrix[y+1][x]))
            if y > 0:
                edges.append(Edge(N*y+x, N*(y-1)+x, matrix[y-1][x]))
            if x < (N-1):
                edges.append(Edge(N*y+x, N*y+x+1, matrix[y][x+1]))
            if x > 0:
                edges.append(Edge(N*y+x, N*y+x-1, matrix[y][x-1]))
    return edges


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

# getting route from source to destination
def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)


# Dijkstra’s algorithm
def findShortestPaths(graph, source, dest, N):

    pq = []
    heappush(pq, Node(source, 0))

    dist = [sys.maxsize] * N
    dist[source] = 0
    done = [False] * N
    done[source] = True

    prev = [-1] * N
    route = []
    weight = 10

    # till min-heap is empty
    while pq:

        node = heappop(pq)
        u = node.vertex

        for edge in graph.adj[u]:
            v = edge.dest
            weight = edge.weight

            # Relaxation step
            if not done[v] and (dist[u] + weight) < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heappush(pq, Node(v, dist[v]))

        done[u] = True

    get_route(prev, dest, route)
    return route


# saving the shortest path to a given file
def save_path(matrix, route, N, path):
    with open(path, 'w') as file:
        for y in range(N):
            for x in range(N):
                if (y*N+x) in route:
                    file.write(str(matrix[y][x]))
                else:
                    file.write(" ")
            file.write("\n")
    file.close()


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('IFILE')
    parser.add_argument('OFILE')
    args = parser.parse_args(arguments[1:])
    input_path = args.IFILE
    output_path = args.OFILE

    N = 6       # size of the grid NxN
    amount = N*N
    val, zero_list = get_val_list(input_path)
    src, dest = zero_list[0], zero_list[1]
    matrix = create_matrix(val, N)
    edges = create_edges_list(matrix, N)
    graph = Graph(edges, amount)
    route = findShortestPaths(graph, src, dest, amount)
    save_path(matrix, route, N, output_path)


if __name__ == '__main__':
    main(sys.argv)
