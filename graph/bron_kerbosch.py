def bron_kerbosch(r, p, x, adj, cliques):
    """
    Bron-Kerbosch algorithm with pivoting to find all maximal cliques.
    """
    if not p and not x:
        cliques.append(r)
        return

    if not p: return

    pivot = max(p | x, key=lambda u: len(adj[u] & p))
    for v in list(p - adj[pivot]):
        bron_kerbosch(r | {v}, p & adj[v], x & adj[v], adj, cliques)
        p.remove(v)
        x.add(v)


if __name__ == "__main__":
    adj = {0: {1, 2}, 1: {0, 2}, 2: {0, 1, 3}, 3: {2}}
    cliques = []
    bron_kerbosch(set(), set(adj.keys()), set(), adj, cliques)
    print(f"Maximal Cliques: {cliques}")
