from matplotlib import pyplot as plt
import networkx as nx


def characteristics(graph):
    # Визначаємо кількість вершин і ребер:
    num_nodes = graph.number_of_nodes()
    num_edges = graph.number_of_edges()
    print(f"\nNodes: {num_nodes}")
    print(f"Edges: {num_edges}")
    print("**********************************************")
    # Визначаємо ступінь вершин (центральність, близькість та посередництво):
    degree_centrality_output = nx.out_degree_centrality(graph)
    degree_centrality_input = nx.in_degree_centrality(graph)
    closeness = nx.closeness_centrality(graph)
    betweenness = nx.betweenness_centrality(graph)
    print(f"Output degree centrality: {degree_centrality_output}")
    print(f"Input degree centrality: {degree_centrality_input}")
    print(f"Closeness: {closeness}")
    print(f"Betweenness: {betweenness}")
    
def show_graph(graph, property, start_node):
    pos = nx.bfs_layout(graph, start=start_node)
    nx.draw(graph, pos, with_labels=True, node_size=4000, node_color="pink", font_size=12, width=2)
    labels = nx.get_edge_attributes(graph, property)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    plt.show()

def init_graph():
    transport_graph = nx.DiGraph()
    transport_graph.add_edge("Київ", "Глеваха", distance=34)
    transport_graph.add_edge("Васильків", "Гребенки", distance=30)
    transport_graph.add_edge("Київ", "Васильків", distance=50)
    transport_graph.add_edge("Київ", "Обухів", distance=47)
    transport_graph.add_edge("Глеваха", "Фастів", distance=48)
    transport_graph.add_edge("Обухів", "Кагарлик", distance=33)
    transport_graph.add_edge("Кагарлик", "Біла Церква", distance=58)
    transport_graph.add_edge("Фастів", "Біла Церква", distance=38)
    transport_graph.add_edge("Глеваха", "Біла Церква", distance=59)
    transport_graph.add_edge("Гребенки", "Біла Церква", distance=20)
    
    return transport_graph


if __name__ == "__main__":
    transport_graph = init_graph()

    show_graph(transport_graph, "distance", 'Київ')
