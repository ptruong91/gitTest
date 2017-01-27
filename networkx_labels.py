import matplotlib.pyplot as plt
import networkx as nx

'CREATE GRAPH'
G=nx.Graph()

G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)



pos = nx.spring_layout(G)

'nodes'
nx.draw_networkx_nodes(G, pos,
                       nodelist=[0,1,2,3],
                       node_color = 'r',
                       node_size = 500,
                       alpha = 0.8)
nx.draw_networkx_nodes(G, pos,
                       nodelist=[4,5,6,7],
                       node_color = 'b',
                       node_size = 800,
                       alpha = 0.7)

'edges'
nx.draw_networkx_edges(G, pos, width = 1.0, alpha=0.5)
nx.draw_networkx_edges(G, pos,
                       edgelist=[(0,1),(1,2),(2,3),(3,0)],
                       width=8, alpha=0.5, edge_color='r')
nx.draw_networkx_edges(G, pos,
                       edgelist=[(4,5),(5,6),(6,7),(7,4)],
                       width=8, alpha=0.5, edge_color='b')


                       


'LABELS'
labels = {}
labels[0] = r'$a$'
labels[1] = r'$test$'
labels[2] = r'$c$'

#nx.draw(G, pos=pos, with_labels=False)
nx.draw_networkx_labels(G,pos,labels)
plt.show()
