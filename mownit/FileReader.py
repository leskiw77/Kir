import csv
import numpy as np


class FileReader:
    def read_csv_file_graph_edges(self, file_name, n):
        a = np.zeros((n, n))
        with open(file_name, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                graph_row = int(row[0])
                graph_col = int(row[1])
                if graph_col >= n or graph_row >= n:
                    raise IndexError('Graph edge out of bound')
                edge_resistance = float(row[2])
                a[graph_row][graph_col] = edge_resistance
        return a

    def read_csv_file_graph_edges_as_tuple(self, file_name, n):
        a = []
        with open(file_name, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                x = int(row[0])
                y = int(row[1])
                if x >= n + 1 or y >= n + 1:
                    raise IndexError('Graph edge out of bound')
                edge_resistance = float(row[2])
                if x > y:
                    a.append((y, x, edge_resistance))
                else:
                    a.append((x, y, edge_resistance))
        return sorted(a, key=lambda x: (x[0], x[1]))


