from collections import deque

class Graph:
    """
    A class to represent a graph using an adjacency list.
    """
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def add_edge(self, vertex, edge):
        """
        Adds an edge to the graph.

        Args:
            vertex: The starting vertex.
            edge: The ending vertex.
        """
        if vertex not in self.gdict:
            self.gdict[vertex] = []
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        """
        Performs Breadth First Search starting from a given vertex.

        Args:
            vertex: The starting vertex for BFS.
        """
        visited = {vertex}
        queue = deque([vertex])
        while queue:
            de_vertex = queue.popleft()
            print(de_vertex)
            for adjacent_vertex in self.gdict.get(de_vertex, []):
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)

    def dfs(self, vertex):
        """
        Performs Depth First Search starting from a given vertex.

        Args:
            vertex: The starting vertex for DFS.
        """
        visited = {vertex}
        stack = [vertex]
        while stack:
            pop_vertex = stack.pop()
            print(pop_vertex)
            for adjacent_vertex in self.gdict.get(pop_vertex, []):
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    stack.append(adjacent_vertex)


if __name__ == "__main__":
    custom_dict = {
        "a": ["b", "c"],
        "b": ["a", "d", "e"],
        "c": ["a", "e"],
        "d": ["b", "e", "f"],
        "e": ["d", "f"],
        "f": ["d", "e"]
    }

    graph = Graph(custom_dict)
    print("BFS starting from 'a':")
    graph.bfs("a")
    print("\nDFS starting from 'a':")
    graph.dfs("a")
