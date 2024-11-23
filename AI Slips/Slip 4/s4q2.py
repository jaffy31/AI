#Write a Python program to implement the Depth-First Search algorithm. Refer to the following graph as input for the program.Initial node: 1  Goal node: 8

from collections import deque

# Define the graph as an adjacency list
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [8],
    6: [8],
    7: [],
    8: []
}

def bfs(graph, start, goal):
    # Create a queue for BFS
    queue = deque([[start]])  # Store paths instead of just nodes
    visited = set()  # Set to keep track of visited nodes
    
    while queue:
        # Dequeue the first path from the queue
        path = queue.popleft()
        node = path[-1]
        
        # Check if the node is already visited
        if node not in visited:
            visited.add(node)
            
            # Check if we reached the goal node
            if node == goal:
                print(f"Path to goal node: {path}")
                return path
            
            # Add paths to the queue for each unvisited neighbor
            for neighbor in graph[node]:
                new_path = path + [neighbor]
                queue.append(new_path)
    
    print("Goal node not found!")
    return None

# Input: Initial node = 1, Goal node = 8
start_node = 1
goal_node = 8

# Call the BFS function
bfs(graph, start_node, goal_node)