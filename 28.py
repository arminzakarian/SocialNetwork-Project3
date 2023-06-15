import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist('ca-AstroPh.txt', comments='#', delimiter='\t')

spl = dict(nx.shortest_path_length(G))
dist = [len([1 for k,v in spl.items() if k!=n and v.get(n) == d]) for n in G.nodes() for d in range(max(spl[n].values())+1)]

plt.bar(range(len(dist)), dist)
plt.title("Shortest path length distribution of Astro Physics collaboration network")
plt.xlabel("Shortest path length")
plt.ylabel("Frequency")
plt.show()

num_nodes = 1000
p = 0.01

er_graph = nx.erdos_renyi_graph(num_nodes, p)

spl = dict(nx.shortest_path_length(er_graph))
dist = [len([1 for k,v in spl.items() if k!=n and v.get(n) == d]) for n in er_graph.nodes() for d in range(max(spl[n].values())+1)]

plt.bar(range(len(dist)), dist)
plt.title("Shortest path length distribution of Erdős-Rényi random graph")
plt.xlabel("Shortest path length")
plt.ylabel("Frequency")
plt.show()

CG = nx.configuration_model(G.degree())
CG = nx.Graph(CG)
spl = dict(nx.shortest_path_length(CG))
dist = [len([1 for k,v in spl.items() if k!=n and v.get(n) == d]) for n in CG.nodes() for d in range(max(spl[n].values())+1)]

plt.bar(range(len(dist)), dist)
plt.title("Shortest path length distribution of Configuration model random graph")
plt.xlabel("Shortest path length")
plt.ylabel("Frequency")
plt.show()

