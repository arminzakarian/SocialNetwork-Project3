#Muhamamd Rahmani Pj3 
import networkx as nx

num_nodes = 18772
num_edges = 198110

G_er = nx.gnm_random_graph(num_nodes, num_edges)
print('# ARMIN ZAKARIAN #')
print('>> Problem 25 Results:')
print(">> Number of nodes:", G_er.number_of_nodes())
print(">> Number of edges:", G_er.number_of_edges())
