from collections import deque


def kahns_topological_sort(n, adj):
    """
    Kahn's algorithm for topological sorting of a DAG.

    Args:
        n (int): Number of vertices.
        adj (list): Adjacency list.

    Returns:
        list: Topological ordering or empty if cycle exists.
    """
    in_degree = [0] * n
    for u in range(n):
        for v in adj[u]:
            in_degree[v] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    res = []
    while queue:
        u = queue.popleft()
        res.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return res if len(res) == n else []


if __name__ == "__main__":
    n = 6
    adj = [[] for _ in range(n)]
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    for u, v in edges:
        adj[u].append(v)
    print(f"Topological Sort: {kahns_topological_sort(n, adj)}")
