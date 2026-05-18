def min_vertex_cover(adj):
    """
    Finds a vertex cover in a graph using 2-approximation algorithm.
    """
    visited = set()
    cover = set()
    edges = []
    for u in adj:
        for v in adj[u]:
            if (v, u) not in edges:
                edges.append((u, v))

    for u, v in edges:
        if u not in visited and v not in visited:
            cover.add(u)
            cover.add(v)
            visited.add(u)
            visited.add(v)
    return cover


if __name__ == "__main__":
    adj = {0: {1, 2}, 1: {0, 2}, 2: {0, 1, 3}, 3: {2}}
    print(f"Vertex Cover (2-approx): {min_vertex_cover(adj)}")
