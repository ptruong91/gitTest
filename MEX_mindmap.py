import matplotlib.pyplot as plt
import networkx as nx

# CREATE GRAPH
G = nx.Graph()

# ADD NODES
G.add_node(0)
G.node[0]['title'] = 'Tracing the Temporal Evolution of Clusters in a Financial Stock Market'
G.node[0]['author'] = 'Argimiro Arratia, Alejandra Cabana'
G.node[0]['market'] = 'Madrid Stock Exhange Market'
G.node[0]['desc'] = ('''
We propose a methodology for clustering financial time series of stocks' returns and
a graphical set-up to quantify and visualise the evolution of these clusters though time.
The porposed graphical repsentation allows for the application of well known algorithms
for solving classical combinatorial graph problems, which can be interpreted as problem
relevant to portfolio design and investment strategies. We illustrate this graph
representation of the evolution of clusters in time and its use on real data from
Madrid Stock Exchange market.
''')

G.add_node(1)
G.node[1]['title'] = 'Tracing the Temporal Evolution of Clusters in a Financial Stock Market'
G.node[1]['author'] = 'Argimiro Arratia, Alejandra Cabana'
G.node[1]['desc'] = ('''
We purpose a methodology
''')

# STORE NODE POSITIONS
pos = nx.spring_layout(G)

# DRAW NODES
nlist = [0,1]

nx.draw_networkx_nodes(G, pos,
                       nodelist=nlist,
                       node_color = 'r',
                       node_size = 500,
                       alpha = 0.8)

# DRAW EDGES
elist = [
    (0,1)
    ]
nx.draw_networkx_edges(G, pos,
                       edgelist=elist,
                       width=8, alpha=0.5, edge_color='r')


labels = {}
labels[0] = r'1.'
labels[1] = r'1.'

nx.draw_networkx_labels(G,pos,labels)
plt.show()
