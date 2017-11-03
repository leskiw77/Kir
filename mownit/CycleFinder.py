import networkx as nx

class CycleFinder:
    def find_cycle(self, edges_list):
        non_zero_edges = [(x, y) for (x, y, _) in edges_list]
        G = nx.Graph(non_zero_edges)
        return list(nx.cycle_basis(G))
