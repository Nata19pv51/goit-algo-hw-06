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


# def dijkstra(graph, start):
#     # Ініціалізація відстаней та множини невідвіданих вершин
#     distances_between_city = {vertex: float('infinity') for vertex in graph}
#     distances_between_city[start] = 0
#     unvisited = set(graph.nodes())
#     # unvisited = list(graph.keys())

#     while unvisited:
#         # Знаходження вершини з найменшою відстанню серед невідвіданих
#         current_vertex = min(unvisited, key=lambda vertex: distances_between_city[vertex])

#         # Якщо поточна відстань є нескінченністю, то ми завершили роботу
#         if distances_between_city[current_vertex] == float('infinity'):
#             break
        
#         for neighbor, attributes in graph.adj[current_vertex].items():
#             if "distance" not in attributes:
#                 continue
                
#             weight = attributes["distance"]
#             new_distance = distances_between_city[current_vertex] + weight 

#             # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
#             if new_distance < distances_between_city[neighbor]:
#                 distances_between_city[neighbor] = new_distance

#         # Видаляємо поточну вершину з множини невідвіданих
#         unvisited.remove(current_vertex)

#     return distances_between_city

def init_graph():
    transport_graph = nx.DiGraph()
    transport_graph.add_edge("Київ", "Глеваха", distance=34, time=49)
    transport_graph.add_edge("Васильків", "Гребенки", distance=30, time=26)
    transport_graph.add_edge("Київ", "Васильків", distance=50, time=50)
    transport_graph.add_edge("Київ", "Обухів", distance=47, time=44)
    transport_graph.add_edge("Глеваха", "Фастів", distance=48, time=42)
    transport_graph.add_edge("Обухів", "Кагарлик", distance=33, time=27)
    transport_graph.add_edge("Кагарлик", "Біла Церква", distance=58, time=55)
    transport_graph.add_edge("Фастів", "Біла Церква", distance=38, time=40)
    transport_graph.add_edge("Глеваха", "Біла Церква", distance=59, time=47)
    transport_graph.add_edge("Гребенки", "Біла Церква", distance=20, time=20)
    
    return transport_graph


if __name__ == "__main__":
    transport_graph = init_graph()
# print(transport_graph.adj["Київ"])
# print(transport_graph.nodes())
# print(transport_graph)
# characteristics(transport_graph)

# search_bfs_iterative(transport_graph, "Київ", "Біла Церква")
# print("\n")
# # search_bfs(transport_graph, deque(["Київ"]), "Біла Церква")
# # print("\n")

    show_graph(transport_graph, "distance", 'Київ')
