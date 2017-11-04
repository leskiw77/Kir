from DrawDirectedGraph import DirectedGraphDraw
from mownit.FileReader import FileReader
import numpy as np
import itertools
from mownit.TupleUtils import TupleUtils

if __name__ == '__main__':
    n = 28
    m = 1
    e = (0, 1, 40)
    e_x, e_y, e_val = e

    file_reader = FileReader()
    edges_tuple = file_reader.read_csv_file_graph_edges_as_tuple('file4.csv', n)
    edges_tuple.append((e_x, e_y, 'e'))
    tuple_utils = TupleUtils(edges_tuple)

    A = np.zeros((n + m - 1, n + m - 1))

    for i in range(1, n):
        neighbours = tuple_utils.get_edges_for_vertex(i)
        x = 0
        for neighbour in neighbours:
            (_, _, val) = neighbour
            if isinstance(val, float):
                x += 1 / val
        A[i - 1][i - 1] = x

    for (x, y, val) in edges_tuple:
        if x > 0 and y > 0 and isinstance(val, float):
            A[x - 1][y - 1] = -1 / val
            A[y - 1][x - 1] = -1 / val

    e_x, e_y, e_val = e

    A[n - 1][e_x - 1] = -1
    A[n - 1][e_y - 1] = 1

    A[e_x - 1][n - 1] = -1
    A[e_y - 1][n - 1] = 1
    A[n - 1][n - 1] = 0

    b = np.zeros(n + m - 1)
    b[n - 1] = e_val
    print(A)
    print(b)
    x = np.linalg.solve(A, b)
    print(x)

    x = list(itertools.chain([0], x))

    result = []
    for (ex, ey, val) in edges_tuple:

        if isinstance(val, float):
            v = (x[ey] - x[ex]) / val
            result.append((ex, ey, v))
    result.append((e_x, e_y, x[n]))

    for_zero = tuple_utils.get_edges_for_vertex(0)
    result = tuple_utils.uniform_direction(result)
    print(result)

    DirectedGraphDraw().draw(result)
