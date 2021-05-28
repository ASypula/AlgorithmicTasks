import sys
import argparse
from typing import Counter
from heapq import heappop, heappush
from Graph_structures import Edge, Graph, Node
from Structures_prep import create_matrix, get_val_list, create_edges_list


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


# getting route from source to destination
def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)


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
