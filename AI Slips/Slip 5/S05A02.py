"""
Breadth-First Search (BFS) Algorithm Implementation

Question:
Write a Python program to implement the Breadth-First Search algorithm. Refer to the following graph as input for the program.
Initial node: 1
Goal node: 8

Graph Representation:
1 is pointing to 2 and 4
2 is pointing to 3
3 is pointing to 4 and 6
4 is pointing to 2
5 is pointing to 7 and 8
6 is pointing to 8
7 is pointing to 8
8 is not pointing to anyone

      2           5 ------
   /  | \      /    \           \
 /    |   \  /         \           7
1     |     3             8 -----
  \   |     /\         /
    \ |   /     \   /
       4           6
"""

from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    if start == goal:
        return f"Initial node and Goal node are the same: {start}"

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            neighbors = graph.get(node, [])
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    return f"Path from {start} to {goal}: {new_path}"

            visited.add(node)

    return f"No path found from {start} to {goal}"

if __name__ == "__main__":
    # Define the graph using an adjacency list
    graph = {
        1: [2, 4],
        2: [3],
        3: [4, 6],
        4: [2],
        5: [7, 8],
        6: [8],
        7: [8],
        8: []
    }

    # Set initial and goal nodes
    initial_node = 1
    goal_node = 8

    # Run BFS algorithm
    result_path = bfs(graph, initial_node, goal_node)

    # Print the result
    print(result_path)
