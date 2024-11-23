"""
 Write a Python program to implement Breadth First Search algorithm. Refer the following 
graph as an Input for the program.[Initial node=1,Goal node=8]
"""

from collections import deque

def bfs(graph, start, goal):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([[start]])  # Queue to manage paths
    visiting_order = []  # List to track the order of visited nodes

    while queue:
        # Get the first path from the queue
        path = queue.popleft()
        node = path[-1]

        # Add the node to the visiting order if not already visited
        if node not in visited:
            visiting_order.append(node)
            visited.add(node)

            # If goal is found, return the path and visiting order
            if node == goal:
                return path, visiting_order

            # Explore its neighbors
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return None, visiting_order  # Return None if no path is found

# Graph representation (adjacency list)
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 4],
    4: [1, 3, 5],
    5: [2, 4, 6, 7],
    6: [5],
    7: [5],
    8: []  # Goal node
}

# Input: Initial node and goal node
start_node = 1
goal_node = 7

# Perform BFS and print the result
path, visiting_order = bfs(graph, start_node, goal_node)
print(f"Visiting order of nodes: {visiting_order}")
if path:
    print(f"Path from node {start_node} to node {goal_node}: {path}")
else:
    print(f"No path found from node {start_node} to node {goal_node}")