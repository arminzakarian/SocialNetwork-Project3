import networkx as nx
import matplotlib.pyplot as plt

G_real = nx.read_edgelist("ca-GrQc.txt")
wcc = nx.weakly_connected_components(G_real)
wcc_sizes = [len(component) for component in wcc]
size_counts = {}
for size in wcc_sizes:
    if size not in size_counts:
        size_counts[size] = 0
    size_counts[size] += 1

total_components = len(wcc_sizes)
size_dist = [size_counts[size] / total_components for size in sorted(size_counts.keys())]
plt.figure(figsize=(10, 5))
plt.plot(sorted(size_counts.keys()), size_dist)
plt.xlabel("Component Size")
plt.ylabel("Distribution")
plt.title("WCC Size Distribution")
plt.show()
