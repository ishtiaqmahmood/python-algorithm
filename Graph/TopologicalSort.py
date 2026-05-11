from collections import defaultdict

class Graph:
    """
    A class to represent a directed graph for Topological Sort.
    """
    def __init__(self, number_of_vertices):
        self.graph = defaultdict(list)
        self.number_of_vertices = number_of_vertices

    def add_edge(self, vertex, edge):
        """
        Adds a directed edge from vertex to edge.

        Args:
            vertex: The starting vertex.
            edge: The ending vertex.
        """
        self.graph[vertex].append(edge)

    def topological_sort_util(self, v, visited, stack):
        """
        A recursive helper function for topological_sort.
        """
        visited.add(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topological_sort_util(i, visited, stack)
        stack.insert(0, v)

    def topological_sort(self):
        """
        Performs topological sort on the graph.
        """
        visited = set()
        stack = []

        # Use list(self.graph) to avoid "dictionary changed size during iteration" if needed,
        # though here we are just reading keys.
        keys = list(self.graph.keys())
        for k in keys:
            if k not in visited:
                self.topological_sort_util(k, visited, stack)
        print(stack)


if __name__ == "__main__":
    custom_graph = Graph(8)
    custom_graph.add_edge("A", "C")
    custom_graph.add_edge("C", "E")
    custom_graph.add_edge("E", "H")
    custom_graph.add_edge("E", "F")
    custom_graph.add_edge("F", "G")
    custom_graph.add_edge("B", "D")
    custom_graph.add_edge("B", "C")
    custom_graph.add_edge("D", "F")

    print("Topological Sort of the graph:")
    custom_graph.topological_sort()
