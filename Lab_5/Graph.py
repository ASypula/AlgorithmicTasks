# creating a matrix from a list of values
def create_matrix(val_list, n):
    matrix = [[0 for x in range(n)]for y in range(n)]
    i = 0
    for y in range(n):
        for x in range(n):
            matrix[y][x] = val_list[i]
            i = i+1
    return matrix

# creating a list of numbers from a grid given in the file
def get_val_list(path):
    val_list = []
    with open(path, 'r') as fp:
        values = fp.read()
        values = values.split()
        for number in values:
            val_list.append(number)
    return val_list


def main():
    val = get_val_list("graph.txt")
    matrix = create_matrix(val, 3)
    print(matrix)

main()