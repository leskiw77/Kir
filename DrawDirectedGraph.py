import matplotlib.pyplot as plt
import networkx as nx


class DirectedGraphDraw:
    def draw(self, edges):
        G = nx.DiGraph()
        for (ex, ey, e_weight) in edges:
            G.add_edge(ex, ey, weight=e_weight)
        plt.figure(figsize=(30, 40))
        plt.subplot(121)
        edge_labels = dict([((u, v,), round(d['weight'], 1))
                            for u, v, d in G.edges(data=True)])

        pos = nx.spring_layout(G)
        nx.draw(G, pos, nodecolor='r', edge_color='b')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        nx.draw_networkx_labels(G, pos)

        plt.show()
