from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dls(self, src, target, max_depth, path):
        path.append(src)  # Add current node to the path
        if src == target:
            return True, path
        if max_depth <= 0:
            path.pop()  # Backtrack
            return False, path

        for neighbor in self.graph[src]:
            found, result_path = self.dls(neighbor, target, max_depth - 1, path)
            if found:
                return True, result_path

        path.pop()  # Backtrack
        return False, path

    def iddfs(self, src, target, max_depth):
        for depth in range(max_depth + 1):
            visited_path = []
            found, path = self.dls(src, target, depth, visited_path)
            print(f"Depth {depth}: Visited Nodes: {visited_path}")
            if found:
                return path
        return None


# Create the graph as per the diagram
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('C', 'G')
g.add_edge('D', 'H')
g.add_edge('D', 'I')
g.add_edge('F', 'K')

# Source node
start = 'A'
goal = 'G'

# Define maximum depth
max_depth = 5

# Run IDDFS
result_path = g.iddfs(start, goal, max_depth)

if result_path:
    print(f"Goal node '{goal}' found with path: {result_path}")
else:
    print(f"Goal node '{goal}' not found within depth {max_depth}")
