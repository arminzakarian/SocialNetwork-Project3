import networkx as nx
import matplotlib.pyplot as plt

G_real = nx.read_edgelist("ca-GrQc.txt")
shortest_path_lengths = nx.shortest_path_length(G_real)
path_length_counts = {}
for source, paths in shortest_path_lengths:
    for target, length in paths.items():
        if length not in path_length_counts:
            path_length_counts[length] = 0
        path_length_counts[length] += 1
total_paths = len(G_real.nodes()) * (len(G_real.nodes()) - 1)
path_length_dist = [path_length_counts[length] / total_paths for length in range(1, max(path_length_counts.keys()) + 1)]
print('# ARMIN ZAKARIAN #')
print('>> PROBLEM RESULTS:')
plt.figure(figsize=(10, 5))
plt.plot(range(1, max(path_length_counts.keys()) + 1), path_length_dist)
plt.xlabel("Shortest Path Length")
plt.ylabel("Distribution")
plt.title("Shortest Path Length Distribution")
plt.show()
print('** DONE **')