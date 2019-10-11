# BFS
from collections import deque

def BFS(G, v, visited):
    queue = deque()
    queue.append(v)
    while len(queue) > 0:
        n = queue.popleft()
        if not visited[n]:
            visited[n] = True
            for u in G[n]:
                if not visited[u]:
                    queue.append(u)


def search(G, v):
    visited = [False] * len(G)
    BFS(G, v, visited)
    for u in G:
        BFS(G, v, visited)


# DFS (Recursive)

def DFS(G, v, visited):
    visited[v] = True
    for u in G[v]:
        if not visited[u]:
            DFS(G, u, visited)

# DFS (Iterative)

def DFS(G, v, visited):
    stack = []
    stack.append(v)
    while len(stack) > 0:
        n = stack.pop()
        if not visited[n]:
            visited[n] = True
            for u in G[n]:
                if not visited[u]:
                    stack.append(u)

# MST -- Kruskals, etc.

# Topological Sort

def search_DFS(G):
    topological_ordering = []
    visited = [0] * len(G)
    for v in range(len(G)):
        topological_dfs(G, v, visited, topological_ordering)
    return list(reversed(topological_ordering))

def topological_dfs(G, v, visited, topological_ordering):
    if visited[v] == 2:
        return
    elif visited[v] == 1:
        raise ValueError("Not a DAG!")
    else:
        visited[v] = 1
        for u in G[v]:
            topological_dfs(G, u, visited, topological_ordering)
        visited[v] = 2
        topological_ordering.append(v)


G = [[1, 3], [4], [0, 4], [4], []]
print(search_DFS(G))




# Iterative Deepening
