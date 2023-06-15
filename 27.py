import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist('ca-AstroPh.txt', comments='#', delimiter='\t')

degree_seq = [d for n, d in G.degree()]
hist = nx.degree_histogram(G)
plt.bar(range(len(hist)), hist)
plt.title("Degree distribution of Astro Physics collaboration network")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()

num_nodes = 1000
p = 0.01

er_graph = nx.erdos_renyi_graph(num_nodes, p)

degree_seq = [d for n, d in er_graph.degree()]
hist = nx.degree_histogram(er_graph)

plt.bar(range(len(hist)), hist)
plt.title("Degree distribution of Erdős-Rényi random graph")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()

CG = nx.configuration_model(G.degree())

CG = nx.Graph(CG)

degree_seq = [d for n, d in CG.degree()]
hist = nx.degree_histogram(CG)

plt.bar(range(len(hist)), hist)
plt.title("Degree distribution of Configuration model random graph")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()
