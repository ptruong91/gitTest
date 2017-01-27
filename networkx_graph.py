import matplotlib.pyplot as plt
import networkx as nx

'CREATE GRAPH'
G = nx.Graph()


'GRAPH ATTRIBUTES'
# Init with attributes
G = nx.Graph(day = "Friday")

#Modify attributes later
G.graph['week'] = '2'

'NODES'
# Create node
G.add_node(1)

# Add list of nodes
G.add_nodes_from([2,3])

# Add any nbunch of nodes
H = nx.path_graph(10)
G.add_nodes_from(H)

# We can have nodes of H as nodes of G
G.add_node(H)

'NODE ATTRIBUTES'
G.add_node(1, time = "5pm")
G.add_nodes_from([3], time = '2pm')
G.node[1]['room'] = 714
print(G.nodes(data=True))

'EDGES'
# Add edge
G.add_edge(1,2)

e=(2,3)
G.add_edge(*e) 

# Add list of edges
G.add_edges_from([(1,2),(1,3)])

# Add ebunch of edges
G.add_edges_from(H.edges())

"DEMOLISH GRAPH"

#G.remove_node(H) #move H node
#G.clear() # clear graph

# FURTHER TESTS
G.add_edges_from([(1,2),(1,3)])
G.add_node(1)
G.add_edge(1,2)
G.add_node("spam") #adds node "spam"
G.add_nodes_from("spam") #adds 4 nodes 's', 'p', 'a', 'm'


# EXAMINE GRAPH
print(G.number_of_nodes())
print(G.number_of_edges())
print(G.nodes())
print(G.edges())
print(G.neighbors(1))

" REMOVING NODES"
G.remove_nodes_from("spam")
print(G.nodes())

# REMOVING EDGES
G.remove_edge(1,3)

'DRAW GRAPH'
#nx.draw(G)
#nx.draw_random(G)
#nx.draw_circular(G)
#nx.draw_spectral(G)
#plt.show()

' CREATE DiGraph using connections from G'
H = nx.DiGraph(G)
print(H.edges)
edgelist= [(0,1), (1,2), (2,3)]
H = nx.Graph(edgelist)


"ACCESSING EDGES"
G.add_edge(2,4)
G[2][4]['color'] = 'blue'

FG = nx.Graph()
FG.add_weighted_edges_from([(1,2,0.125), (1,3,0.75), (2,4,1.2), (3,4,0.375)])

#print out edges with less weight than 0.5, undirected is looks at each edge twice
for n,nbrs in FG.adjacency_iter():
    for nbr, eattr in nbrs.items():
        data = eattr['weight']
        if data < 0.5: print('(%d, %d, %.3f)' %(n, nbr, data))

#same as above but compacter
for (u,v,d) in FG.edges(data='weight'):
    if d<0.5: print('(%d, %d, %.3f)'%(n,nbr,d))

"EDGE ATTRIBUTES"
G.add_edge(1,2,weight=4.7)
G.add_edges_from([(3,4),(4,5)], color = 'red')
G.add_edges_from([(1,2,{'color':'blue'}), (2,3,{'weight':8})])
G[1][2]['weight'] = 4.7
G.edge[1][2]['weight'] = 4
        
"DRAW GRAPH"
#nx.draw(H)
nx.draw(G)
#nx.draw(FG)
plt.show()


