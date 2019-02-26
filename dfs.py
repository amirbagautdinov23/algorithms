graph1 = {
    'A': ['B', 'S'],
    'B': ['A'],
    'C': ['D', 'E', 'F', 'S'],
    'D': ['C'],
    'E': ['C', 'H'],
    'F': ['C'],
    'G': ['S'],
    'H': ['E'],
    'S': ['A', 'C', 'G']
}

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
            print(visited)
    return visited

visited = dfs(graph1,'A', [])
print(visited)