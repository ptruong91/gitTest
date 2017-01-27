import matplotlib.pyplot as plt
import networkx as nx

DG = nx.DiGraph()
DG.add_weighted_edges_from([(1,2,0.5),(3,1,0.75)])
DG.out_degree(1, weight = 'weight')

nx.draw(DG)
plt.show()
