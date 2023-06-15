
import urllib.request
import gzip
import networkx as nx
import matplotlib.pyplot as plt

url = "https://snap.stanford.edu/data/ca-GrQc.txt.gz"
file_name = "ca-GrQc.txt.gz"
urllib.request.urlretrieve(url, file_name)

with gzip.open(file_name, 'rb') as gz_file:
    with open("ca-GrQc.txt", 'wb') as output_file:
        output_file.write(gz_file.read())

G_real = nx.read_edgelist("ca-GrQc.txt")
G_small_world = nx.watts_strogatz_graph(len(G_real.nodes()), len(G_real.edges()), 0.1)
degree_dist_real = nx.degree_histogram(G_real)
degree_dist_small_world = nx.degree_histogram(G_small_world)
plt.figure(figsize=(10, 5))
plt.plot(degree_dist_real, label="Real World Graph")
plt.plot(degree_dist_small_world, label="Small World Graph")
plt.xlabel("Degree")
plt.ylabel("Count")
plt.title("Degree Distribution")
plt.legend()
plt.show()