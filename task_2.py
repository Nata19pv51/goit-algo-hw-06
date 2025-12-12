from collections import deque
from task_1 import init_graph, show_graph


def search_dfs_iterative(graph, start_node, target_node=None):
    visited = set()
    # Використовуємо стек для зберігання вершин
    stack = [start_node]  
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()
        
        if vertex == target_node:
            print(vertex, end=' ')
            visited.add(vertex)
            return vertex
              
        if vertex not in visited:
            print(vertex, end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(list(graph[vertex]))) 
            
def search_bfs_iterative(graph, start_node, target_node=None):
    queue = deque([start_node])
    visited = {start_node}
    # Словник для відновлення шляху
    path = {start_node: [start_node]} 

    while queue:
        u = queue.popleft()
        print(u, end=' ')
        if u == target_node:
            return path[u]

        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)

                path[v] = path[u] + [v]

if __name__ == "__main__":
    graph = init_graph()
    
    print("************************************* BFS ************************************")
    search_bfs_iterative(graph, "Київ")
    print("\n")
    search_bfs_iterative(graph, "Київ", "Гребенки")
    print("\n")
    search_bfs_iterative(graph, "Київ", "Біла Церква")
    print("\nBFS - DONE")
    
    print("************************************* DFS ************************************")
    search_dfs_iterative(graph, "Київ")
    print("\n")
    search_dfs_iterative(graph, "Київ", "Гребенки")
    print("\n")
    search_dfs_iterative(graph, "Київ", "Біла Церква")
    print("\nDFS - DONE")
    
    show_graph(graph, "distance", "Київ")
