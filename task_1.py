from matplotlib import pyplot as plt
import networkx as nx


G = nx.DiGraph()
G.add_edge("Київ", "Васильків", distance=50, time=50)
G.add_edge("Київ", "Обухів", distance=47, time=44)
G.add_edge("Київ", "Глеваха", distance=34, time=49)
G.add_edge("Васильків", "Гребенки", distance=30, time=26)
G.add_edge("Глеваха", "Фастів", distance=48, time=42)
G.add_edge("Обухів", "Кагарлик", distance=33, time=27)
G.add_edge("Кагарлик", "Біла Церква", distance=58, time=55)
G.add_edge("Фастів", "Біла Церква", distance=38, time=40)
G.add_edge("Глеваха", "Біла Церква", distance=59, time=47)
G.add_edge("Гребенки", "Біла Церква", distance=20, time=20)

# Визначаємо кількість вершин і ребер:
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
print(f"Nodes: {num_nodes}")
print(f"Edges: {num_edges}")

# Визначаємо ступінь вершин:
degree_centrality_output = nx.out_degree_centrality(G)
degree_centrality_input = nx.in_degree_centrality(G)
closeness = nx.closeness_centrality(G)
betweenness = nx.betweenness_centrality(G)
print(f"Output degree centrality: {degree_centrality_output}")
print(f"Input degree centrality: {degree_centrality_input}")
print(f"Closeness: {closeness}")
print(f"Betweenness: {betweenness}")

pos = nx.spring_layout(G, seed=44)
nx.draw(G, pos, with_labels=True, node_size=4000, node_color="pink", font_size=12, width=2)
labels = nx.get_edge_attributes(G, "distance")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()
