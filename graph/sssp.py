from collections import deque

class Graph:
    """
    A class to represent a graph for Single Source Shortest Path (SSSP) using BFS.
    """
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):
        """
        Finds the shortest path between start and end nodes using BFS.

        Args:
            start: The starting vertex.
            end: The ending vertex.

        Returns:
            list: The shortest path from start to end.
        """
        queue = deque([[start]])
        visited = {start}

        while queue:
            path = queue.popleft()
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                if adjacent not in visited:
                    visited.add(adjacent)
                    new_path = list(path)
                    new_path.append(adjacent)
                    queue.append(new_path)


if __name__ == "__main__":
    custom_dict = {
        "a": ["b", "c"],
        "b": ["d", "g"],
        "c": ["d", "e"],
        "d": ["f"],
        "e": ["f"],
        "g": ["f"]
    }

    g = Graph(custom_dict)
    print(f"Shortest path from 'a' to 'e': {g.bfs('a', 'e')}")
