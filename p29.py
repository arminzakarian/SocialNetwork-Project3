from typing import Any

import matplotlib.pyplot as plt
import networkx as nx
import psutil

G_real = nx.read_edgelist('ca-AstroPh.txt')
n = 18772  # Number of nodes
m = 198110  # Number of edges
G_erdos = nx.gnm_random_graph(n, m)
degree_seq = [G_real.degree(node) for node in G_real.nodes()]
G_config = nx.configuration_model(degree_seq)
degree_dist_real = nx.degree_histogram(G_real)
degree_dist_erdos = nx.degree_histogram(G_erdos)
degree_dist_config = nx.degree_histogram(G_config)
shortest_path_lengths_real = nx.shortest_path_length(G_real)
path_lengths_real: list[Any] = [length for lengths in shortest_path_lengths_real.values() for length in lengths.values()]
shortest_path_lengths_erdos = nx.shortest_path_length(G_erdos)
path_lengths_erdos = [length for lengths in shortest_path_lengths_erdos.values() for length in lengths.values()]
shortest_path_lengths_config = nx.shortest_path_length(G_config)
path_lengths_config = [length for lengths in shortest_path_lengths_config.values() for length in lengths.values()]
clustering_coeffs_real = nx.clustering(G_real)
clustering_coeffs_values_real = list(clustering_coeffs_real.values())
clustering_coeffs_erdos = nx.clustering(G_erdos)
clustering_coeffs_values_erdos = list(clustering_coeffs_erdos.values())
clustering_coeffs_config = nx.clustering(G_config)
clustering_coeffs_values_config = list(clustering_coeffs_config.values())

plt.plot(degree_dist_real, 'bo-', label='Real World Graph')
plt.plot(degree_dist_erdos, 'ro-', label='Erdos-Renyi Graph')
plt.plot(degree_dist_config, 'go-', label='Configuration Model Graph')
plt.xlabel('Degree')
plt.ylabel('Count')
plt.title
