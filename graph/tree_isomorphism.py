def get_tree_hash(u, p, adj):
    child_hashes = []
    for v in adj[u]:
        if v != p:
            child_hashes.append(get_tree_hash(v, u, adj))
    return "(" + "".join(sorted(child_hashes)) + ")"


def are_isomorphic(adj1, adj2, n):
    """
    Checks if two trees are isomorphic using canonical hashing.
    """
    # Assuming trees are rooted at 0 for simplicity.
    # For general case, find centers of both trees and root them at centers.
    return get_tree_hash(0, -1, adj1) == get_tree_hash(0, -1, adj2)


if __name__ == "__main__":
    tree1 = [[1, 2], [0], [0]]
    tree2 = [[1], [0, 2], [1]]
    print(f"Isomorphic? {are_isomorphic(tree1, tree2, 3)}")
