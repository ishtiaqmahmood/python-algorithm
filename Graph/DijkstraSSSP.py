from collections import defaultdict
import heapq

class Graph:
    """
    A class to represent a weighted graph for Dijkstra's Algorithm.
    """
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        """
        Adds a node to the graph.

        Args:
            value: The value of the node.
        """
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        """
        Adds a weighted edge between two nodes.

        Args:
            from_node: The starting node.
            to_node: The ending node.
            distance (int or float): The weight of the edge.
        """
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    """
    Performs Dijkstra's algorithm to find the shortest paths from an initial node.

    Args:
        graph (Graph): The graph to search.
        initial: The starting node.

    Returns:
        tuple: (visited distances, path predecessors)
    """
    visited = {initial: 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = [min_node]  # Store the predecessor

    return visited, path


if __name__ == "__main__":
    custom_graph = Graph()
    nodes = ["A", "B", "C", "D", "E", "F", "G"]
    for node in nodes:
        custom_graph.add_node(node)

    custom_graph.add_edge("A", "B", 2)
    custom_graph.add_edge("A", "C", 5)
    custom_graph.add_edge("B", "C", 6)
    custom_graph.add_edge("B", "D", 1)
    custom_graph.add_edge("B", "E", 3)
    custom_graph.add_edge("C", "F", 8)
    custom_graph.add_edge("D", "E", 4)
    custom_graph.add_edge("E", "G", 9)
    custom_graph.add_edge("F", "G", 7)

    distances, paths = dijkstra(custom_graph, "A")
    print(f"Distances from A: {distances}")
    print(f"Predecessors: {dict(paths)}")
