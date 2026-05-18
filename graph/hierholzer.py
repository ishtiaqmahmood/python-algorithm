def find_eulerian_circuit(adj):
    """
    Hierholzer's algorithm to find an Eulerian circuit.

    Args:
        adj (dict): Adjacency list (multi-graph supported).

    Returns:
        list: Eulerian circuit.
    """
    stack = [next(iter(adj))]
    circuit = []
    while stack:
        u = stack[-1]
        if adj[u]:
            v = adj[u].pop()
            # For undirected graph, we would also need to remove (v, u)
            stack.append(v)
        else:
            circuit.append(stack.pop())
    return circuit[::-1]


if __name__ == "__main__":
    adj = {0: [1], 1: [2], 2: [0]}
    print(f"Eulerian Circuit: {find_eulerian_circuit(adj)}")
