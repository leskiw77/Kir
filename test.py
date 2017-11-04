import matplotlib.pyplot as plt
import networkx as nx
G = nx.cubical_graph()
plt.subplot(121)
nx.draw(G) # default spring_layout
plt.subplot(122)
nx.draw(G, pos=nx.circular_layout(G), nodecolor='r', edge_color='b')