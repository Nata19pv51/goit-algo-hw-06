def search_dfs(graph, node, visited = None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node, end = ' ')
    
    for friend in graph[node]:
        if friend not in visited:
            search_dfs(graph, friend, visited)

def search_bfs():
    pass