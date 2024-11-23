#Write a Python program to implement the Depth-First Search algorithm. Refer to the following graph as input for the program. Initial node: 1  Goal node: 8

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

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
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)
    graph.add_edge(3, 7)
    graph.add_edge(5, 8)
    graph.add_edge(4, 8)
    graph.add_edge(6, 8)
    graph.add_edge(7, 8)

    initial_node = 1
    goal_node = 8

    result_path = dfs(graph.graph, initial_node, goal_node)

    if result_path:
        print(f"Path from {initial_node} to {goal_node}: {result_path}")
    else:
        print(f"No path found from {initial_node} to {goal_node}")
