class TupleUtils:
    def __init__(self, edges_tuple):
        self.edges_tuple = edges_tuple

    def get_index_by_x_y(self, x, y):
        if x > y:
            raise Exception('dont know')

        for (i, (xx, yy, _)) in enumerate(self.edges_tuple):
            if x == xx and y == yy:
                return i
        return -1

    def get_edges_for_vertex(self, v):
        edges = []
        for (x, y, val) in self.edges_tuple:
            if x == v or y == v:
                edges.append((x, y, val))
        return edges

    def get_resistance_by_x_y(self, x, y):
        if x > y:
            raise Exception('dont know')

        for (xx, yy, r) in self.edges_tuple:
            if x == xx and y == yy:
                return r
        raise ImportError('No such edge')

    def return_if_e_in_edge(self,e, x, y):
        (e_x, e_y, e_val) = e
        if x == e_x and y == e_y:
            return e_val
        if x == e_y and y == e_x:
            return -e_val
        return 0

