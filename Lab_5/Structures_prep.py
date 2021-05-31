from Graph_structures import Edge


# creating a matrix from a list of values
def create_matrix(val_list, n):
    matrix = [[0 for x in range(n)]for y in range(n)]
    i = 0
    for y in range(n):
        for x in range(n):
            matrix[y][x] = val_list[i]
            i = i+1
    return matrix


# creating a list of numbers from a grid given in the file, returns also places with 0's and size of the grid
def get_val_list(path):
    val_list = []
    zero_list = []
    count = 0
    size = 0
    with open(path, 'r') as fp:
        values = fp.read()
        for line in values:
            for number in line:
                if (number == '\n'):
                    size = size+1
                    continue
                val_list.append(int(number))
                if int(number) == 0:
                    zero_list.append(count)
                count = count+1
    return val_list, zero_list, size


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
