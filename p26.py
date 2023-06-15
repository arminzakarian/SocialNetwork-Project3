import networkx as nx
import urllib.request
import matplotlib.pyplot as plt

url = "http://snap.stanford.edu/data/ca-AstroPh.txt.gz"
filename = "ca-AstroPh.txt.gz"
urllib.request.urlretrieve(url, filename)

G_real = nx.read_edgelist(filename)

degrees = [d for (n, d) in G_real.degree()]
G_config = nx.configuration_model(degrees)

G_config = nx.Graph(G_config)

print("Real-world graph:")
print("Number of nodes:", G_real.number_of_nodes())
print("Number of edges:", G_real.number_of_edges())

print("\nConfiguration Model random graph:")
print("Number of nodes:", G_config.number_of_nodes())
print("Number of edges:", G_config.number_of_edges())

plt.figure(figsize=(8, 6))
nx.draw(G_real, node_size=20)
plt.title("Real-world graph")
plt.show()

plt.figure(figsize=(8, 6))
nx.draw(G_config, node_size=20)
plt.title("Configuration Model random graph")
plt.show()
