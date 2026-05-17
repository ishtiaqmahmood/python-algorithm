import heapq

def prims_algorithm(graph, start_node):
    """
    Finds the Minimum Spanning Tree of a weighted undirected graph.

    Args:
        graph (dict): Adjacency list {node: [(neighbor, weight), ...]}.
        start_node: Starting node.

    Returns:
        list: Edges in the MST.
    """
    mst = []
    visited = {start_node}
    edges = [(weight, start_node, neighbor) for neighbor, weight in graph[start_node]]
    heapq.heapify(edges)

    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            for neighbor, next_weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(edges, (next_weight, v, neighbor))
    return mst


if __name__ == "__main__":
    test_graph = {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 1), ('D', 1), ('E', 4)],
        'C': [('A', 3), ('B', 1), ('F', 5)],
        'D': [('B', 1), ('E', 1)],
        'E': [('B', 4), ('D', 1), ('F', 1)],
        'F': [('C', 5), ('E', 1)]
    }
    print(f"MST Edges (Prim's): {prims_algorithm(test_graph, 'A')}")
