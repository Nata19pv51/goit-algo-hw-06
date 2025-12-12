from collections import deque
from task_1 import init_graph, show_graph


def search_dfs_iterative(graph, start_node, target_node=None):
    visited = set()
    stack = [start_node]
    # використовуємо словник для зберігання батьківського вузла
    parent = {start_node: None} 

    while stack:
        u = stack.pop() 

        if u not in visited:
            print(u, end=' ')
            visited.add(u)

            if u == target_node:
                print("\n")
                return _reconstruct_path(parent, target_node)
            
            # використовуємо reversed, щоб дотримуватися порядку
            for v in reversed(list(graph[u])):
                if v not in visited:
                    # додаємо сусідів до стеку
                    stack.append(v)
                    # встановлюємо, що u є батьком v
                    parent[v] = u 
                    
    return None

# Функція для відновлення шляху
def _reconstruct_path(parent, target_node):
    path = []
    current = target_node
    while current is not None:
        path.append(current)
        current = parent.get(current)
    return path[::-1] # Повертаємо шлях у правильному порядку (від start до target)

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
    print("\n")
    return path

if __name__ == "__main__":
    graph = init_graph()
    
    print("************************************* BFS ************************************")
    print(search_bfs_iterative(graph, "Київ"))
    print("\n")
    print(search_bfs_iterative(graph, "Київ", "Гребенки"))
    print("\n")
    print(search_bfs_iterative(graph, "Київ", "Біла Церква"))
    print("\nBFS - DONE")
    
    print("************************************* DFS ************************************")
    print(search_dfs_iterative(graph, "Київ"))
    print("\n")
    print(search_dfs_iterative(graph, "Київ", "Гребенки"))
    print("\n")
    print(search_dfs_iterative(graph, "Київ", "Біла Церква"))
    print("\nDFS - DONE")
    
    show_graph(graph, "distance", "Київ")
