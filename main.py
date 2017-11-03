import numpy as np
from mownit.CycleFinder import CycleFinder
from mownit.FileReader import FileReader
from mownit.TupleUtils import TupleUtils


def first_kirchow_law():
    for i in range(0, n-1):
        for (x, y, val) in tuple_utils.get_edges_for_vertex(i):
            pos = tuple_utils.get_index_by_x_y(x, y)
            if x == i:
                val = 1
            else:
                val = -1
            A[i][pos] = val


def second_kirchow_law():
    for i in range(0, edges_number - n + 1):
        cycle = cycle_list[i]
        cycle_len = len(cycle)
        for v in range(0, cycle_len):
            x = cycle[v]
            y = cycle[(v + 1) % cycle_len]
            electro = tuple_utils.return_if_e_in_edge(e, x, y)
            if electro != 0:
                b[edges_number - i - 1] = -electro

            val = 1
            if y < x:
                x, y = y, x
                val = -1
            pos = tuple_utils.get_index_by_x_y(x, y)
            r = tuple_utils.get_resistance_by_x_y(x, y)

            A[edges_number - i - 1][pos] = val * r


if __name__ == '__main__':
    n = 8
    e = (0, 1, 40)

    file_reader = FileReader()
    edges_tuple = file_reader.read_csv_file_graph_edges_as_tuple('file.csv', n)
    cycle_list = CycleFinder().find_cycle(edges_tuple)
    edges_number = len(edges_tuple)

    A = np.zeros((edges_number, edges_number))
    b = np.zeros(edges_number)
    tuple_utils = TupleUtils(edges_tuple)

    first_kirchow_law()
    second_kirchow_law()

    x = np.linalg.solve(A, b)
    print(x)
