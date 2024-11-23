#Write a Python program to implement the Depth-First Search algorithm. Refer to the following graph as input for the program. Initial node: 1, Goal node: 7

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].extend(neighbors)

def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path = path + [start]

    if start == goal:
        return path

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, visited, path)
            if new_path:
                return new_path

    return None

if __name__ == "__main__":
    # Define the graph
    graph = Graph()
    graph.add_edge(1, [3, 2])
    graph.add_edge(2, [4])
    graph.add_edge(3, [2])
    graph.add_edge(4, [5, 6])
    graph.add_edge(5, [3, 7])
    graph.add_edge(7, [6])

    # Set initial and goal nodes
    initial_node = 1
    goal_node = 7

    # Run DFS algorithm
    result_path = dfs(graph.graph, initial_node, goal_node)

    # Print the result
    if result_path:
        print(f"Path from {initial_node} to {goal_node}: {result_path}")
    else:
        print(f"No path found from {initial_node} to {goal_node}")
