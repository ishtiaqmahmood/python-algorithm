def tarjan_scc(num_nodes, adj):
    """
    Finds Strongly Connected Components using Tarjan's algorithm.

    Args:
        num_nodes (int): Number of nodes.
        adj (dict): Adjacency list.

    Returns:
        list: List of SCCs.
    """
    timer = 0
    tin = [-1] * num_nodes
    low = [-1] * num_nodes
    stack = []
    on_stack = [False] * num_nodes
    sccs = []

    def dfs(u):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        stack.append(u)
        on_stack[u] = True

        for v in adj.get(u, []):
            if tin[v] == -1:
                dfs(v)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:
                low[u] = min(low[u], tin[v])

        if low[u] == tin[u]:
            current_scc = []
            while True:
                node = stack.pop()
                on_stack[node] = False
                current_scc.append(node)
                if node == u: break
            sccs.append(current_scc)

    for i in range(num_nodes):
        if tin[i] == -1:
            dfs(i)
    return sccs


if __name__ == "__main__":
    g = {0: [2, 3], 1: [0], 2: [1], 3: [4], 4: []}
    print(f"SCCs (Tarjan): {tarjan_scc(5, g)}")
