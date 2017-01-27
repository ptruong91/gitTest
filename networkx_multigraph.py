import matplotlib.pyplot as plt
import networkx as nx

MG = nx.MultiGraph()
MG.add_weighted_edges_from([(1,2,.5), (1,2,.75), (2,3,.5)])
print(MG.degree(weight='weight'))

nx.draw(MG)
plt.show()

K_5=nx.complete_graph(5)
nx.draw(K_5)
plt.show()
