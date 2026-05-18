def biconnected_components(n, adj):
    """
    Finds biconnected components in an undirected graph.
    """
    visited = [False] * n
    discovery = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    stack = []
    time = 0
    res = []

    def dfs(u):
        nonlocal time
        discovery[u] = low[u] = time
        time += 1
        visited[u] = True
        children = 0

        for v in adj[u]:
            if not visited[v]:
                children += 1
                parent[v] = u
                stack.append((u, v))
                dfs(v)
                low[u] = min(low[u], low[v])
                if (parent[u] == -1 and children > 1) or (parent[u] != -1 and low[v] >= discovery[u]):
                    component = []
                    while stack[-1] != (u, v):
                        component.append(stack.pop())
                    component.append(stack.pop())
                    res.append(component)
            elif v != parent[u] and discovery[v] < discovery[u]:
                stack.append((u, v))
                low[u] = min(low[u], discovery[v])

    for i in range(n):
        if not visited[i]:
            dfs(i)
            if stack:
                component = []
                while stack: component.append(stack.pop())
                res.append(component)
    return res


if __name__ == "__main__":
    adj = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
    print(f"Biconnected Components: {biconnected_components(4, adj)}")
