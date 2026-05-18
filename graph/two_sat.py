def get_scc(n, adj):
    visited = [False] * n
    stack = []
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]: dfs1(v)
        stack.append(u)

    for i in range(n):
        if not visited[i]: dfs1(i)

    rev_adj = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]: rev_adj[v].append(u)

    scc = [-1] * n
    count = 0
    def dfs2(u, c):
        scc[u] = c
        for v in rev_adj[u]:
            if scc[v] == -1: dfs2(v, c)

    while stack:
        u = stack.pop()
        if scc[u] == -1:
            dfs2(u, count)
            count += 1
    return scc


def solve_2sat(n, clauses):
    """
    Solves 2-Satisfiability problem.
    Clauses are (a, b) where a, b are literals (1 to n or -1 to -n).

    Args:
        n (int): Number of variables.
        clauses (list): List of clauses.

    Returns:
        list: Variable assignments or None.
    """
    adj = [[] for _ in range(2 * n)]
    for a, b in clauses:
        # a v b <=> (~a => b) and (~b => a)
        u = n + a - 1 if a > 0 else -a - 1
        v = n + b - 1 if b > 0 else -b - 1
        not_u = n - a - 1 if a > 0 else n + (-a) - 1
        not_v = n - b - 1 if b > 0 else n + (-b) - 1
        adj[not_u].append(v)
        adj[not_v].append(u)

    scc = get_scc(2 * n, adj)
    res = [False] * n
    for i in range(n):
        if scc[i] == scc[i + n]:
            return None
        res[i] = scc[i] > scc[i + n]
    return res


if __name__ == "__main__":
    clauses = [(1, 2), (-1, 3), (-2, -3)]
    print(f"2-SAT Solution: {solve_2sat(3, clauses)}")
