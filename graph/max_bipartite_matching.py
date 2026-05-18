def dfs(u, adj, match_y, visited):
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            if match_y[v] < 0 or dfs(match_y[v], adj, match_y, visited):
                match_y[v] = u
                return True
    return False


def max_bipartite_matching(nx, ny, adj):
    """
    Finds the maximum bipartite matching using DFS.
    """
    match_y = [-1] * ny
    result = 0
    for i in range(nx):
        visited = [False] * ny
        if dfs(i, adj, match_y, visited):
            result += 1
    return result


if __name__ == "__main__":
    adj = [[0, 1], [0], [2]]
    print(f"Max Matching: {max_bipartite_matching(3, 3, adj)}")
