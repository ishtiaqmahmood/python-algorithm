import heapq


def bellman_ford(n, edges, s):
    dist = [float('inf')] * n
    dist[s] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None
    return dist


def dijkstra(n, adj, s):
    dist = [float('inf')] * n
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist


def johnsons_algorithm(n, adj):
    """
    Johnson's algorithm for All-Pairs Shortest Paths.
    """
    edges = []
    for u in range(n):
        for v, w in adj[u]:
            edges.append((u, v, w))

    # Add virtual node
    v_edges = edges + [(n, i, 0) for i in range(n)]
    h = bellman_ford(n + 1, v_edges, n)
    if h is None: return None

    new_adj = [[] for _ in range(n)]
    for u in range(n):
        for v, w in adj[u]:
            new_adj[u].append((v, w + h[u] - h[v]))

    dist_matrix = []
    for i in range(n):
        d = dijkstra(n, new_adj, i)
        for j in range(n):
            if d[j] != float('inf'):
                d[j] = d[j] + h[j] - h[i]
        dist_matrix.append(d)
    return dist_matrix


if __name__ == "__main__":
    adj = {0: [(1, -5), (2, 2), (3, 3)], 1: [(2, 4)], 2: [], 3: [(2, 1)]}
    print(f"APSP Johnson's: {johnsons_algorithm(4, adj)}")
